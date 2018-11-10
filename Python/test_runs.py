import PySimpleGUI as sg

# sg.SetOptions(element_padding=(10, 2))

sg.ChangeLookAndFeel('DarkBlue')

layout = [[sg.Text(' Add New Class', font=("Helvetica", 25))],
          [sg.Text('Code Code', pad=(75, 2), font=("Helvetica", 15))],
          [sg.Input((), size=(10, 2), pad=(50, 0))],
          [sg.Text(' Period Number', font=("Helvetica", 15))],
          [sg.Input((), size=(20, 2), pad=((20, 0), 10))],
          [sg.Text('Year', font=("Helvetica", 15))],
          [sg.DropDown((2016, 2017, 2018, 2019), size=(20, 2))],
          [sg.ReadButton('Course Code', size=(20, 2), pad=(45, 0))]
          ]

window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)

event, values = window.Read()
