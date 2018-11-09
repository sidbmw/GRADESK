import PySimpleGUI as sg

student_name = 'Mike Dong'
mark = [[],
        []]

column = [[sg.Text('Expectation  ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],
[sg.Text('Mark            ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],
[sg.Text('                  ', justification = 'right'), sg.Checkbox(' ')],
[sg.Text('_'  * 100, size=(23, 1))]]





layout = [[sg.Text('Mark entry - ' + student_name, size=(21, 1), font=("Helvetica", 15), justification = 'center')],
[sg.Radio('Test             ', 'RADIO1', default=True, text_color = 'red'), sg.Radio('Assignment   ', 'RADIO1', text_color = 'blue')],
[sg.Radio('Presentation ', 'RADIO1', text_color = 'green'), sg.Radio('Quiz           ', 'RADIO1', text_color = 'Yellow'), sg.Checkbox(' ')],
[sg.Column(column,scrollable=True, size=(225,150))]]


event, values  = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
