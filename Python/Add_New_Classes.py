# author: Siddharth Natamai, edited and altered: Mike Dong, Late October
# version: 2.2

import cx_Oracle
import PySimpleGUI as sg
from Add_Students import run_program as add_student
from input_checker import check_string


def run_program():  # the function that runs everything
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # connects to the database
    cur = con.cursor(scrollable=True)  # object, used to execute SQL commands in python

    layout = [[sg.Text('Add New Classes', size=(30, 2), justification='center', font=("Helvetica", 25))],  # where the gui is put together, each [] means that its a line's content
              [sg.Text('  Course Code', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.Input((), size=(20, 2), pad=((215, 150), 10))],
              [sg.Text('   Period Number', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.Input((), size=(20, 2), pad=((215, 150), 10))],
              [sg.Text('Year', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.DropDown((2016, 2017, 2018, 2019), size=(18, 2), pad=((214, 150), 10))],
              [sg.ReadButton('Add Course', key='add_new_courses_button', size=(20, 2), pad=((205, 150), 10),
                             bind_return_key=True)]
              ]

    window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)  # used to open up a window and display everything

    while 'add_new_courses_button':  # runs if the button is pressed or set to False by pressing it
        event, values = window.Read()  # the pysimplegui equivalent of an action listener
        if event is None or event == 'Exit':  # closes itself
            break
        v_course_code = values[0]
        v_period_num = values[1]
        v_year = values[2]

        if len(str(v_course_code)):  # checks if the course code is proper
            cur.execute("select * from EOM_CLASS")
            for row in cur:  # goes through the class table
                if v_course_code + '/' + v_year == (row[0]):  # check if there' a class like this one already in the data base
                    sg.Popup("This is already a class with same name and active year")
                    break

        if v_course_code != '' and v_period_num != '' and v_year != '':  # check to see if the inputs are blank
            if check_string(v_course_code, 'str', 8) and check_string(v_period_num, 'int', 4)\
                    and check_string(v_year, 'int', 2025):  # check if input is acceptable

                cur.execute("""
                     insert into EOM_CLASS (CLASS, PERIOD_NUM)
                     values (:v_course_code, :v_period_num)""",

                            v_course_code=v_course_code + '/' + v_year,
                            v_period_num=v_period_num
                            )
                con.commit()

                add_student(v_course_code + '/' + v_year)

                window.Close()
            else:
                sg.Popup('Incorrect data format, try again.')
        else:
            sg.Popup("Please complete input")
