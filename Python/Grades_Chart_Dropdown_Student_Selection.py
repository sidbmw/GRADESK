import cx_Oracle
import PySimpleGUI as sg

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

cur.execute("SELECT LAST_NAME || ', ' || FIRST_NAME FROM EOM_STUDENTS")
full_name = cur.fetchall()
full_name = [n[0] for n in full_name]
# print(full_name)

cur.execute("SELECT COUNT(*) FROM EOM_STUDENTS")
num_of_rows = cur.fetchall()
num_of_rows = [n[0] for n in num_of_rows]
num_of_rows = num_of_rows[0]
# print(num_of_rows)

# i = 0
# first_name = ''
# while i < num_of_rows:
#     first_name = first_name + str(full_name[i].split(", "))
#     i += 1
# print(first_name)


layout = [[sg.Text('Listbox with search')],
          [sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_INPUT_')],
          [sg.Listbox(full_name, size=(60, 10), enable_events=True, key='_LIST_')],
          [sg.Button('Exit')]]

window = sg.Window('Window Title').Layout(layout)

while True:  # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    # print(event, values)

    if values['_INPUT_'] != '':
        search = values['_INPUT_']
        new_values = [x for x in full_name if search in x]
        window.Element('_LIST_').Update(new_values)
    else:
        window.Element('_LIST_').Update(full_name)

    if event == '_LIST_' and len(values['_LIST_']):
        sg.Popup('Selected ', values['_LIST_'])

        # print(values['_LIST_'][0])
        full_name_split = values['_LIST_'][0].split(", ")
        last_name = full_name_split[0]
        first_name = full_name_split[1]

        # print(first_name)

        cur.execute("SELECT STUDENT_ID, CLASS FROM EOM_STUDENTS WHERE FIRST_NAME = :first_name AND LAST_NAME = :last_name", first_name=first_name, last_name=last_name)
        student_id_and_class = cur.fetchall()
        student_id = [n[0] for n in student_id_and_class]
        student_id = student_id[0]
        class_code = [n[1] for n in student_id_and_class]
        class_code = class_code[0]

        # student id and class code fetched from selected name (in dropdown menu)
        print(student_id, class_code)

window.Close()
