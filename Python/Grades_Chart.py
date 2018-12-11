import cx_Oracle
import PySimpleGUI as sg
import pandas as pd
import sys

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)


# WIP FOR LISTBOX
cur.execute("SELECT FIRST_NAME FROM EOM_STUDENTS")
names_fetch = cur.fetchall()

for row in names_fetch:
    print(row)

names = [
#
]

# layout = [[sg.Text('Listbox with search')],
#           [sg.Input(do_not_clear=True, size=(20, 1), enable_events=True, key='_INPUT_')],
#           [sg.Listbox(names, size=(20, 4), enable_events=True, key='_LIST_')],
#           [sg.Button('Exit')]]
#
# window = sg.Window('Window Title').Layout(layout)
#
# while True:  # Event Loop
#     event, values = window.Read()
#     if event is None or event == 'Exit':
#         break
#     print(event, values)
#     if values['_INPUT_'] != '':
#         search = values['_INPUT_']
#         new_values = [x for x in names if search in x]
#         window.Element('_LIST_').Update(new_values)
#     else:
#         window.Element('_LIST_').Update(names)
#     if event == '_LIST_' and len(values['_LIST_']):
#         sg.Popup('Selected ', values['_LIST_'])
#
# window.Close()
