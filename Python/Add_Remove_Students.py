# !/usr/bin/env python
import cx_Oracle

import PySimpleGUI as sg

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

sg.ChangeLookAndFeel('DarkBlue')

# cur.execute("SELECT  CLASS FROM EOM_CLASS")
# fetch_course_code = cur.fetchall()
# fetched_course_codes = [n[0] for n in fetch_course_code]
# print(fetched_course_codes)

number_Of_Students = sg.PopupGetText("Number of Students")
scrollable_column = [[sg.InputText(), sg.InputText(), sg.Button(button_text=" X ")]]

for x in range(int(number_Of_Students) - 1):
    scrollable_column = scrollable_column + [[sg.InputText(), sg.InputText(), sg.Button(button_text=" X ")]]
    print(x)

layout = [[sg.Stretch(), sg.Text('Add Students', font=("Helvetica", 25)), sg.Stretch()],
          [sg.Stretch(), sg.Text('Course code needs to be fetched into here')],
          [sg.Text("                              First Name"), sg.Text("                                                      Last Name")],
          [sg.Column(scrollable_column, scrollable=True, size=(650, 500), vertical_scroll_only=True)],
          # [sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_INPUT_')],
          # [sg.Listbox(fetched_course_codes, size=(20, 4), enable_events=True, key='_LIST_')],

          [sg.Stretch(), sg.ReadButton('Add Students', key='key_add_students', size=(20, 2),
                                       bind_return_key=True), sg.Stretch(), ]
          ]

window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)

while 'key_add_students':
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

    for x in (number_Of_Students + 1):
        cur.execute("SELECT EOM_STUDENTS_S.nextval from DUAL")
        nextval_fetched = cur.fetchall()
        print(nextval_fetched)

    # cur.execute(
    #     "INSERT INTO EOM_STUDENTS (STUDENT_ID, CLASS, FIRST_NAME, LAST_NAME) VALUES (EOM_STUDENTS_S.currval, 'TESTB-01/2018', 'Mike', 'Dong')")

    con.commit()

window.Close()
