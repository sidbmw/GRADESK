import PySimpleGUI as sg
import marking_first
import cx_Oracle

con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

def getName(x):

    cur.execute("select * from EOM_STUDENTS")
    for row in cur:
        if int(x) == (row[0]):
           return str(row[2]+ " " + row[3])

studentID = 1

student_name = getName(studentID)
mark = [[],
        []]
column = []  # part of the layout

sg.ChangeLookAndFeel('DarkBlue')

for x in range(int(marking_first.numberOfMark)):
    column.append(
        [sg.Text('Expectation  ', text_color='black', justification='left'), sg.InputText('', size=(10, 1))], )
    column.append(
        [sg.Text('Mark            ', text_color='black', justification='left'), sg.InputText('', size=(10, 1))], )
    column.append([sg.Text('_' * 100, size=(23, 1))], )

layout = [[sg.Text('Mark entry - ' + student_name + ", " + marking_first.nameOfMark, size=(21, 1),
                   font=("Helvetica", 15), justification='center')],
          [sg.Column(column, scrollable=True, size=(225, 300))],
          [sg.Button('Previous Student', key='key_prev_stud'), sg.Button('Save', key='key_save'),
           sg.Button('Next Student', key='key_next_stud')]]

window = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

while (True):
    # This is the code that reads and updates your window
    event, values = window.Read()

    if event == 'key_save':

        for x in range(int(marking_first.numberOfMark)):
            tracker = int(x * 2)
            if values[tracker + 0] != None:
                if values[tracker + 1] != None:
                    mark[0].append(values[tracker + 0])
                    mark[1].append(values[tracker + 1])
                else:
                    sg.Popup('incomplete input')
            else:
                sg.Popup('incomplete input')

        sg.Popup(mark[0], mark[1])

    if event == 'Quit' or values is None:
        break

window.Close()  # Don't forget to close your window!


