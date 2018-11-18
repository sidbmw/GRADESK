# Author: Siddharth Natamai
# Date: November 10, 2018

# !/usr/bin/env python
import cx_Oracle

import PySimpleGUI as sg

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

sg.ChangeLookAndFeel('DarkBlue')

layout = [[sg.Text('Add New Classes', size=(30, 2), justification='center', font=("Helvetica", 25))],
          [sg.Text('  Course Code', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.Input((), size=(20, 2), pad=((215, 150), 10))],
          [sg.Text('   Period Number', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.Input((), size=(20, 2), pad=((215, 150), 10))],
          [sg.Text('Year', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.DropDown((2016, 2017, 2018, 2019), size=(18, 2), pad=((214, 150), 10))],
          [sg.ReadButton('Add Course', key='add_new_courses_button', size=(20, 2), pad=((205, 150), 10),
                         bind_return_key=True)]
          ]

window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)

while 'add_new_courses_button':
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    v_course_code = values[0]
    v_period_num = values[1]
    v_year = values[2]
    print(v_course_code, v_period_num, v_year)
    break
window.Close()

# sql = "INSERT INTO EOM_CLASS (CLASS, YEAR, PERIOD_NUM) VALUES (%s, %d, %d)"
# val = ('v_course_Code', 'v_year', 'v_period_Number')
#
# cur.execute(sql, val)
#
# # cur.prepare('INSERT INTO EOM_CLASS (CLASS, YEAR, PERIOD_NUM) VALUES (:CLASS ,:YEAR , :PERIOD_NUM)')
# # cur.execute({'CLASS': v_course_Code}, {'YEAR': v_year}, {'PERIOD_NUM': v_period_Number})
#
#
# # q = "INSERT INTO EOM_CLASS (CLASS, YEAR, PERIOD_NUM) VALUES(:CLASS, :YEAR, :PERIOD_NUM)"
# #
# # cur.execute(q, CLASS=v_course_Code, YEAR=v_year, PERIOD_NUM=v_period_Number)

# for i in range(1):
cur.execute("""

     insert into EOM_CLASS (CLASS, YEAR, PERIOD_NUM)
     values (:v_course_code, :v_year, :v_period_num)""",

            v_course_code=values[0],
            v_year=values[1],
            v_period_num=values[2]
            )
con.commit()
