import PySimpleGUI as sg


student_name = 'Mike Dong'
mark = [[],
        []]

column = []

#column.remove([sg.RealtimeButton('Add')])

column.append([sg.Text('Expectation  ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],)
column.append([sg.Text('Mark            ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],)
column.append([sg.Text('                  ', justification = 'right'), sg.Checkbox(' ')],)
column.append([sg.Text('_'  * 100, size=(23, 1))],)
column.append([sg.Button('Add', size = (23,2), key = 'key_add')],)

layout = [[sg.Text('Mark entry - ' + student_name, size=(21, 1), font=("Helvetica", 15), justification = 'center')],
[sg.Radio('Test             ', 'RADIO1', default=True, text_color = 'red'), sg.Radio('Assignment   ', 'RADIO1', text_color = 'blue')],
[sg.Radio('Presentation ', 'RADIO1', text_color = 'green'), sg.Radio('Quiz           ', 'RADIO1', text_color = 'Yellow'), sg.Checkbox(' ')],
[sg.Column(column,scrollable=True, size=(225,150))],
[sg.Button('Previous Student', key = 'key_prev_stud'), sg.Button('Save', key = 'key_save'), sg.Button('Next Student', key = 'key_next_stud')]]

window  = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

while (True):
    # This is the code that reads and updates your window
    event, values = window.Read()
    if 'key_add':
         #values[0], is the Test radio, values[1] is the Assignment, and so on one at a time

        del column[len(column)-1]
        column.append([sg.Text('Expectation  ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],)
        column.append([sg.Text('Mark            ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],)
        column.append([sg.Text('                  ', justification = 'right'), sg.Checkbox(' ')],)
        column.append([sg.Text('_'  * 100, size=(23, 1))],)
        column.append([sg.Button('Add', size = (23,2), key = 'key_add')],)
        window  = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    if event == 'Quit'  or values is None:
        break

window.Close()  # Don't forget to close your window!
