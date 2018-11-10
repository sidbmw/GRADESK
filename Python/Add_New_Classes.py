# Author: Siddharth Natamai
# Date: November 10, 2018

# !/usr/bin/env python


import PySimpleGUI as sg

# sg.SetOptions(element_padding=(0, 0))

sg.ChangeLookAndFeel('DarkBlue')

layout = [[sg.Text('Add New Classes', size=(30, 2), justification='center', font=("Helvetica", 25))],
          [sg.Text('Course Code', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.Input((), size=(20, 2), pad=((205, 150), 10))],
          [sg.Text('Period Number', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.Input((), size=(20, 2), pad=((205, 150), 10))],
          [sg.Text('Year', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.DropDown((2016, 2017, 2018, 2019), size=(20, 2), pad=((205, 150), 10))],
          [sg.ReadButton('Course Code', key='add_new_courses_button', size=(20, 2), pad=((205, 150), 10))]
          ]

window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)

event, values = window.Read()
