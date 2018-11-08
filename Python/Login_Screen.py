# Author: Siddharth Natamai
# Date: November 7, 2018

# !/usr/bin/env python


import PySimpleGUI as sg





layout = [[sg.Text('GRADESK', size=(30, 1), pad=((5, 5), 3), justification='center', font=("Helvetica", 25))],
          [sg.Text('Username', size=(30, 1), pad=((154, 150), 3), justification='center', )],
          [sg.Input(pad=((150, 150), 3))],
          [sg.Text('Password', size=(30, 1), pad=((154, 150), 3), justification='center', )],
          [sg.Input(pad=((150, 150), 3))],
          [sg.Button('Read', bind_return_key=True), sg.Exit()]]

window = sg.Window('Enter Login Credentials', default_element_size=(40, 1)).Layout(layout)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if (values[0] == 'test') & (values[1] == 'test'):
        print('Login SUCCESSFUL')
    else:
        print('Login FAILED!!')
        print(values)
    print(event, values)
window.Close()
