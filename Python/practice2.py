import PySimpleGUI as sg

numberOf = 1

student_name = 'Mike Dong'
mark = [[],
        []]

column = [[sg.Button('Add', size=(23,2))]]


#column.remove([sg.Button('Add', size=(23,2))])
del column[len(column)-1]

for x in range(numberOf):
    column.append([sg.Text('Expectation  ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],)
    column.append([sg.Text('Mark            ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],)
    column.append([sg.Text('                  ', justification = 'right'), sg.Checkbox(' ')],)
    column.append([sg.Text('_'  * 100, size=(23, 1))],)
    column.append([sg.Button('Add', size=(23,2), bind_return_key = True)],)


layout = [[sg.Text('Mark entry - ' + student_name, size=(21, 1), font=("Helvetica", 15), justification = 'center')],
[sg.Radio('Test             ', 'RADIO1', default=True, text_color = 'red'), sg.Radio('Assignment   ', 'RADIO1', text_color = 'blue')],
[sg.Radio('Presentation ', 'RADIO1', text_color = 'green'), sg.Radio('Quiz           ', 'RADIO1', text_color = 'Yellow'), sg.Checkbox(' ')],
[sg.Column(column,scrollable=True, size=(225,150))]]

#event, values  = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
window = sg.FlexForm('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

while True:
    event, values = window.Read()
    if event is None:
        break
