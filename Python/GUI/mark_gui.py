import PySimpleGUI as sg
import marking_first
import cx_Oracle

#con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
#cur = con.cursor(scrollable=True)
student_name = 'Mike Dong'
mark = [[],
        []]




column = []

#column.remove([sg.RealtimeButton('Add')])
sg.ChangeLookAndFeel('DarkBlue')

for x in range(int(marking_first.numberOfMark)):
    column.append([sg.Text('Expectation  ', text_color = 'black', justification = 'left'), sg.InputText(' ', size= (10, 1))],)
    column.append([sg.Text('Mark            ', text_color = 'black', justification = 'left'), sg.InputText(mark[[0],[x]], size= (10, 1))],)
    column.append([sg.Text('_'  * 100, size=(23, 1))],)

layout = [[sg.Text('Mark entry - ' + student_name, size=(21, 1), font=("Helvetica", 15), justification = 'center')],
[sg.Column(column,scrollable=True, size=(225,300))],
[sg.Button('Previous Student', key = 'key_prev_stud'), sg.Button('Save', key = 'key_save'), sg.Button('Next Student', key = 'key_next_stud')]]

window  = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

while (True):
    # This is the code that reads and updates your window
    event, values = window.Read()



    if event == 'Quit'  or values is None:
        break

window.Close()  # Don't forget to close your window!
