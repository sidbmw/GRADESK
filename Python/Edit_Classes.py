# !/usr/bin/env python
import cx_Oracle
import PySimpleGUI as sg
from Edit_Students import do_it as edit
from input_checker import check_string as check_string

old_class = ''
old_period_number = 0


def do_it(x, y, z):
    student_numbers = []

    def get_rows(course_code):  # both fills the array with student ids and gets the amount of students

        cur.execute("select * from EOM_STUDENTS")
        v_row = 0
        for row in cur:
            if row[1] == course_code:
                v_row += 1
                student_numbers.append(row[0])

        return v_row

    con = cx_Oracle.connect('system/EOM@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)
    sg.ChangeLookAndFeel('DarkBlue')

    global old_class
    global old_period_number

    old_class = str(x + '/' + z)
    old_period_number = int(y)

    layout = [[sg.Text('Edit Classes - ' + x, size=(30, 2), justification='center', font=("Helvetica", 25))],
              [sg.Text('  Course Code', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.Input(x, size=(20, 2), pad=((215, 150), 10))],
              [sg.Text('   Period Number', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.Input(y, size=(20, 2), pad=((215, 150), 10))],
              [sg.Text('Year', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.DropDown((2016, 2017, 2018, 2019), size=(18, 2), pad=((214, 150), 10), default_value=int(z))],
              [sg.Button('Edit Course', key='edit_courses_button', size=(20, 2), pad=((205, 150), 10),)],
              [sg.Button('Go to Edit Students', key='edit_student_key', size=(20, 2), pad=((205, 150), 10),)]
              ]

    window = sg.Window('Edit Courses', default_element_size=(40, 2)).Layout(layout)

    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break

        if event == 'edit_courses_button':

            if values[0] != '' and values[1] != '' and values[2] != '':
                if check_string(values[0], 'str', 8) and check_string(values[1], 'int', 4) \
                        and check_string(values[2], 'int', 2025):

                    cur.execute("UPDATE EOM_CLASS SET PERIOD_NUM = :v_period_num WHERE CLASS = :old_course", v_period_num=values[1],
                                old_course=old_class)

                    cur.execute("UPDATE EOM_CLASS SET CLASS = :v_class WHERE CLASS = :old_course", v_class=values[0] + '/' + values[2],
                                old_course=old_class)

                    for x in range(int(get_rows(old_class))-1):
                        cur.execute("UPDATE EOM_STUDENTS SET CLASS = :new_class WHERE STUDENT_ID = :other_stuff",
                                    new_class=values[0] + '/' + values[2],
                                    other_stuff=student_numbers[x])

                    con.commit()

                    break

        if event == 'edit_student_key':
            edit(old_class)

    window.Close()
