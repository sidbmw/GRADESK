# author: Siddharth Natamai, Earl December
# version: 1.4

import cx_Oracle
import PySimpleGUI as sg


def run_program(course):  # the function that runs everything
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # connects to the database
    cur = con.cursor(scrollable=True)
    number_of_students = int(sg.PopupGetText("Number of Students"))
    scrollable_column = [[sg.Input(), sg.Input()]]

    for x in range(int(number_of_students) - 1):
        scrollable_column = scrollable_column + [[sg.Input(), sg.Input(), sg.Button(button_text=" X ")]]

    layout = [[sg.Stretch(), sg.Text('Add Students', font=("Helvetica", 25)), sg.Stretch()],
              [sg.Stretch(), sg.Text('Course code needs to be fetched into here')],
              [sg.Text("                              First Name"),
               sg.Text("                                                      Last Name")],
              [sg.Column(scrollable_column, scrollable=True, size=(650, 500), vertical_scroll_only=True)],
              # [sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_INPUT_')],
              # [sg.Listbox(fetched_course_codes, size=(20, 4), enable_events=True, key='_LIST_')],

              [sg.Stretch(), sg.Button('Add Students', key='key_add_students', size=(20, 2)),
               sg.Text("Save occurs only once 'Add Student' button is pressed"), sg.Stretch()]
              ]

    window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)

    while True:
        print('running')
        event, values = window.Read()
        if event is None or event == 'Exit':
            break

        for x in range(1, (int(number_of_students) + 1)):
            v_pos = x * 2 + 1
            student_first_name = values[v_pos]
            student_last_name = values[v_pos + 1]

            cur.execute(
                """INSERT INTO EOM_STUDENTS (STUDENT_ID, CLASS, FIRST_NAME, LAST_NAME) VALUES (EOM_STUDENTS_S.nextval, :course, :student_first_name, :student_last_name)""",
                student_first_name=student_first_name,
                course=course,
                student_last_name=student_last_name
            )

        sg.Popup("Student names have been stored in database")
        cur.callproc('eom_student_sort')
        con.commit()
        break

    window.Close()
