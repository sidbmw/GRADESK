# !/usr/bin/env python
import cx_Oracle
import PySimpleGUI as sg

old_class = ''
old_period_number = 0


def do_it(x, y, z):
    con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
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
              [sg.ReadButton('Edit Course', key='edit_courses_button', size=(20, 2), pad=((205, 150), 10),
                             bind_return_key=True)]
              ]

    window = sg.Window('Edit Courses', default_element_size=(40, 2)).Layout(layout)

    while 'edit_courses_button':
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        v_class = values[0] + '/' + values[2]
        v_period_num = values[1]

        print(old_class)
        print(old_period_number)

        cur.execute("UPDATE EOM_CLASS SET CLASS = :v_class WHERE CLASS = :stuff", v_class=values[0] + '/' + values[2],
                    stuff=old_class)

        cur.execute("UPDATE EOM_CLASS SET CLASS = :v_period_num WHERE CLASS = :other_stuff", v_period_num=values[1],
                    other_stuff=old_period_number)

        print(v_class, v_period_num)
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
