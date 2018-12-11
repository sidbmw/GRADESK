
# !/usr/bin/env python
import cx_Oracle
import PySimpleGUI as sg

old_course_code = ''
old_period_number = 0
old_year = 0


def do_it(x,y,z):
    con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)
    sg.ChangeLookAndFeel('DarkBlue')

    global old_course_code
    global old_period_number
    global old_year

    old_course_code = x
    old_period_number = y
    old_year = int(z)



    layout = [[sg.Text('Edit Classes - ' + x, size=(30, 2), justification='center', font=("Helvetica", 25))],
              [sg.Text('  Course Code', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.Input(x, size=(20, 2), pad=((215, 150), 10))],
              [sg.Text('   Period Number', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.Input(y, size=(20, 2), pad=((215, 150), 10))],
              [sg.Text('Year', size=(50, 1), justification='center', font=("Helvetica", 15))],
              [sg.DropDown((2016, 2017, 2018, 2019), size=(18, 2), pad=((214, 150), 10), default_value=int(z))],
              [sg.ReadButton('Edit Course', key='edit_courses_button', size=(20, 2), pad=((205, 150), 10),
                             bind_return_key=True)]
              ]

    window = sg.Window('Edit Courses', default_element_size=(40, 2)).Layout(layout)

    while 'edit_courses_button':
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        v_course_code = values[0]
        v_period_num = values[1]
        v_year = values[2]

        sql_bit = "UPDATE EOM_CLASS SET CLASS = v_course_code WHERE CLASS = old_course_code"

        print(v_course_code, v_period_num, v_year)

        cur.execute(sql_bit)
        # for row in cur:
        #     if v_course_code == (row[0]):
        #         sg.Popup("INVALID")
        #         break
        #
        # cur.execute("""
        #
        #          insert into EOM_CLASS (CLASS, YEAR, PERIOD_NUM)
        #          values (:v_course_code, :v_year, :v_period_num)""",
        #
        #             v_course_code=values[0],
        #             v_year=values[2],
        #             v_period_num=values[1]
        #             )

        con.commit()

        break

    window.Close()

