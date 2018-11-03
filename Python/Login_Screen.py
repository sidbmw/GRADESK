# Author: sidbmw
# Date: November 3, 2018

#!/usr/bin/env python

import PySimpleGUI as sg

layout = [[sg.Text('GRADESK', size=(30, 1), justification='center', font=("Helvetica", 25))],
          [sg.Text('Username')],
          [sg.Input()],
          [sg.Text('Password')],
          [sg.Input()],
          [sg.Button('Read', bind_return_key=True), sg.Exit()]]


window = sg.Window('Enter Login Credentials', default_element_size=(40, 1)).Layout(layout)


while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if values[0] == 'test':
        print('Login SUCCESSFUL')
    else:
        print('Login FAILED!!')
        print(values)
    print(event, values)
window.Close()
