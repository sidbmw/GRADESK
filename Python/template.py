import sys

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


column = [
            [sg.Button('Button 1'), sg.Text('This is panel 2')],
            [sg.Button('Button 2')],
            [sg.Button('Button 3')],
            [sg.Button('Button 4')],
            [sg.Button('Button 5')],
            [sg.Button('Button 6')],
            [sg.Button('Button 7')],
            [sg.Button('Button 8')],
            [sg.Button('Button 9')],
            [sg.Button('Button 10')],
         ]

layout = [[sg.Text('This is panel 1')],
          [sg.Column(column,scrollable=True, size=(300,200) )],]

window = sg.Window('Window Title').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window.FindElement('_OUTPUT_').Update(values['_IN_'])

window.Close()
