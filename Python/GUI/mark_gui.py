import PySimpleGUI as sg

mark = [[],
        []]

column = []


layout = [[sg.Text('Mark entry', size=(17, 1), font=("Helvetica", 25), justification = 'center')],
[sg.Radio('Test    ', 'RADIO1', default=True, text_color = 'red'), sg.Radio('Assignment    ', 'RADIO1', text_color = 'blue'), sg.Radio('Presentation    ', 'RADIO1', text_color = 'green'), sg.Radio('Quiz    ', 'RADIO1', text_color = 'Yellow'), sg.Checkbox(' ')]]


event, values  = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
