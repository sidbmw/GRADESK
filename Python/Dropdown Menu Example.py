import cx_Oracle
import PySimpleGUI as sg


con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)


cur.execute("SELECT FIRST_NAME FROM EOM_STUDENTS")
names_fetch = cur.fetchall()

new_names = [n[0] for n in names_fetch]
print(new_names)

layout = [[sg.Text('Listbox with search')],
          [sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_INPUT_')],
          [sg.Listbox(new_names, size=(20, 4), enable_events=True, key='_LIST_')],
          [sg.Button('Chrome'), sg.Button('Exit')]]

window = sg.Window('Window Title').Layout(layout)

while True:  # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    print(event, values)
    if values['_INPUT_'] != '':
        search = values['_INPUT_']
        new_values = [x for x in new_names if search in x]
        window.Element('_LIST_').Update(new_values)
    else:
        window.Element('_LIST_').Update(new_names)
    if event == '_LIST_' and len(values['_LIST_']):
        sg.Popup('Selected ', values['_LIST_'])

window.Close()
