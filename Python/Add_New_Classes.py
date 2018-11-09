import PySimpleGUI as sg

sg.ChangeLookAndFeel('DarkBlue')

layout = [[sg.Text('Add New Courses', size=(30, 1), justification='center', font=("Helvetica", 25))],
          [sg.DropDown('1, 2, 3, 4, 5, 6')]
]

window = sg.Window('Add New Courses', default_element_size=(40, 1)).Layout(layout)

event, values = window.Read()