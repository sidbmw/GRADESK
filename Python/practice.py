#Author: Siddharth Natamai
#Date: November 2, 2018

#!/usr/bin/env python


import PySimpleGUI as sg

layout = [[sg.Text('GRADESK', size=(30, 1), justification='center', font=("Helvetica", 25))],
          [sg.Input()],
          [sg.OK()] ]

sg.Window('Enter login credentials').Layout(layout).Read()
