
# !/usr/bin/env python


import PySimpleGUI as sg

# sg.SetOptions(element_padding=(0, 0))

sg.ChangeLookAndFeel('DarkBlue')

layout = [[sg.Text('Students ', size=(30, 1), justification='center', font=("Helvetica", 25))],
          [sg.Text('  ICS4U.01 2018', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.Input((), size=(20, 2), pad=((215, 150), 10))],
          [sg.Text('   Period Number', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.Input((), size=(20, 2), pad=((215, 150), 10))],
          [sg.Text('Year', size=(50, 1), justification='center', font=("Helvetica", 15))],
          [sg.DropDown((2016, 2017, 2018, 2019), size=(18, 2), pad=((214, 150), 10))],
          [sg.ReadButton('Done', key='add_new_courses_button', size=(20, 2), pad=((205, 150), 10),
                         bind_return_key=True)]
          ]

window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)

event, values = window.Read()
