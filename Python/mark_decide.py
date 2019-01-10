import PySimpleGUI as sg
import cx_Oracle
import sys
from mark_gui import do_it as for_class
from mark_gui_single import do_it as for_single


def do_it(course, student_number):
    def get_name(x):
        cur.execute("select * from EOM_STUDENTS")
        for row in cur:
            if x == (row[0]):
                return str(row[2] + " " + row[3])

    con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)

    sg.ChangeLookAndFeel('DarkBlue')

    student_name = get_name(student_number)

    layout = [[sg.Text('New assessment for whole class or just ' + student_name + '?', size=(20, 2),
                       font=("Helvetica", 12), justification='center')],
             [sg.Text('   ')],
              [sg.Button('For whole class', key='key_class'),
               sg.Button('For ' + student_name + ' only', key='key_single')]]

    window = sg.Window('Mark ', auto_size_text=True, default_element_size=(50, 2)).Layout(layout)

    while True:
        event, values = window.Read()
        if event == 'key_single':
            for_single(course, student_number)
            break

        if event == 'key_class':
            for_class(course)
            break

        if values is None:
            sys.exit()


do_it('ICS4U-01/2018', 5)




