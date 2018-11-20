
import PySimpleGUI as sg
import cx_Oracle

sql = """

"""

layout = [[sg.Text('GRADESK', size=(30, 1), justification='center', font=("Helvetica", 25))],
          [sg.Text('        Username', size=(30, 1), pad=((154, 150), 3), justification='center')],
          [sg.Input(pad=((150, 150), 3))],
          [sg.Text('        Password', size=(30, 1), pad=((154, 150), 3), justification='center')],
          [sg.Input(pad=((150, 150), 3), password_char='*')],
          [sg.Button('Read', key='Read_Key'), sg.Exit()]]

window = sg.Window('Enter Login Credentials', default_element_size=(40, 1)).Layout(layout)

while 'Read_Key':
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if (values[0] == 'EOM') & (values[1] == 'EOM'):
        print('Login SUCCESSFUL')
        con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
        print("Connected to Database")
        print(con.version)
        con.close()
        sg.Popup("Login Successful, Connected to Database")
        break
    if values[0] != 'EOM':
        print('Login FAILED!!')
        sg.Popup("Login Failed")
        print(values[0], values[1])
        # print(event, values)
window.Close()
