# author: Mike Dong, Late November
# version: 3.0

import cx_Oracle
import PySimpleGUI as sg
from Edit_Students import run_program as edit
from input_checker import check_string as check_string

old_class = ''  # variable, holds the current name of the class
old_period_number = 0  # variable, holds the current period number of the class


def run_program(name, period, year):  # the function that runs everything
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # connects to the database
    cur = con.cursor(scrollable=True)  # object, used to execute SQL commands in python

    student_numbers = []  # list, the student_numbers of the students in the given class

    def get_number(course_code):  # function, get the amount of students and fill the student_numbers array
        cur.execute("select * from EOM_STUDENTS")
        v_row = 0
        for row in cur:  # goes through the students table
            if row[1] == course_code:  # check if this student is in the given class
                v_row += 1
                student_numbers.append(row[0])
        return v_row

    global old_class
    global old_period_number

    old_class = str(name + '/' + year)
    old_period_number = int(period)

    layout = [[sg.Text('Edit Classes - ' + name, size=(30, 2), justification='center', font=("Helvetica", 25))],
              # where the gui is put together, each [] means that its a line's content
              [sg.Text('  Course Code', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.Input(name, size=(20, 2), pad=((215, 150), 10))],
              [sg.Text('   Period Number', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.Input(period, size=(20, 2), pad=((215, 150), 10))],
              [sg.Text('Year', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.DropDown((2016, 2017, 2018, 2019), size=(18, 2), pad=((214, 150), 10), default_value=int(year))],
              [sg.Button('Edit Course', key='edit_courses_button', size=(20, 2), pad=((205, 150), 10), )],
              [sg.Button('Go to Edit Students', key='edit_student_key', size=(20, 2), pad=((205, 150), 10), )]
              ]

    window = sg.Window('Edit Courses', default_element_size=(40, 2)).Layout(layout)  # used to open up a window and display everything

    while True:  # runs as long as the window is open, similar to an action listener
        event, values = window.Read()  # the pysimplegui equivalent of an action listener
        if event is None or event == 'Exit':
            break

        if event == 'edit_courses_button':  # checks if it was the edit classes button that was pressed

            if check_string(values[0], 'str', 8) and check_string(values[1], 'int', 4) \
                    and check_string(values[2], 'int', 2025):  # check if the inputs are valid

                cur.execute("UPDATE EOM_CLASS SET PERIOD_NUM = :v_period_num WHERE CLASS = :old_course", v_period_num=values[1],
                            old_course=old_class)

                cur.execute("UPDATE EOM_CLASS SET CLASS = :v_class WHERE CLASS = :old_course", v_class=values[0] + '/' + values[2],
                            old_course=old_class)

                for x in range(int(get_number(old_class)) - 1):  # runs once for every student in the old_class to change their class to the new class
                    cur.execute("UPDATE EOM_STUDENTS SET CLASS = :new_class WHERE STUDENT_ID = :other_stuff",
                                new_class=values[0] + '/' + values[2],
                                other_stuff=student_numbers[x])

                con.commit()

                break
            else:
                sg.Popup('Invalid input')

        if event == 'edit_student_key':  # checks if it was the edit students button that was pressed
            edit(old_class)

    window.Close()
