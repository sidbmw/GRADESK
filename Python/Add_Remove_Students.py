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

scrollable_column = [[sg.InputText(), sg.Button(button_text=" X ")]]

for x in range(int(number_Of_Students) - 1):
    scrollable_column = scrollable_column + [[sg.InputText(), sg.Button(button_text=" X ")]]
    print(number_Of_Students)

layout = [[sg.Stretch(), sg.Text('Add/Remove Students', font=("Helvetica", 25)), sg.Stretch()],
          [sg.Stretch(), sg.Text('Course code needs to be fetched into here')],
          [sg.Column(scrollable_column, scrollable=True, size=(350, 200))],
          # [sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_INPUT_')],
          # [sg.Listbox(fetched_course_codes, size=(20, 4), enable_events=True, key='_LIST_')],

          [sg.Stretch(), sg.ReadButton('Add Course', key='add_new_courses_button', size=(20, 2),
                                       bind_return_key=True), sg.Stretch(), ]
          ]

window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)

while 'add_new_courses_button':
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    # if values['_INPUT_'] != '':
    #     search = values['_INPUT_']
    #     new_values = [x for x in fetched_course_codes if search in x]
    #     window.Element('_LIST_').Update(new_values)
    # else:
    #     window.Element('_LIST_').Update(fetched_course_codes)
    # if event == '_LIST_' and len(values['_LIST_']):
    #     sg.Popup('Selected ', values['_LIST_'])
    if event == 'key_add_students':
        reopen = True
        for x in range(len(classes)):
            if values[x]:
                cur.execute("DELETE FROM EOM_CLASS WHERE CLASS = :stuff", stuff=str(classes[x] + '/' + year[x]))

        con.commit()
        break
window.Close()
