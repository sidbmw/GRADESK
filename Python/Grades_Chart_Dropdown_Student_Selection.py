import cx_Oracle
import PySimpleGUI as sg

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

cur.execute("SELECT LAST_NAME FROM EOM_STUDENTS")
last_name = cur.fetchall()
last_name = [n[0] for n in last_name]
print(last_name)

cur.execute("SELECT FIRST_NAME FROM EOM_STUDENTS")
first_name = cur.fetchall()
first_name = [n[0] for n in first_name]
print(first_name)

full_name = ''
for i in range(0, len(first_name)):
    full_name += last_name[i] + str(", ") + first_name[i] + str('    ')

print(full_name)

# full_name = last_name + str(", ") + first_name

layout = [[sg.Text('Listbox with search')],
          [sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_INPUT_')],
          [sg.Listbox(full_name, size=(60, 10), enable_events=True, key='_LIST_')],
          [sg.Button('Chrome'), sg.Button('Exit')]]


window = sg.Window('Window Title').Layout(layout)

while True:  # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    print(event, values)

    if values['_INPUT_'] != '':
        search = values['_INPUT_']
        new_values = [x for x in full_name if search in x]
        window.Element('_LIST_').Update(new_values)
    else:
        window.Element('_LIST_').Update(full_name)

    if event == '_LIST_' and len(values['_LIST_']):
        sg.Popup('Selected ', values['_LIST_'])

window.Close()
