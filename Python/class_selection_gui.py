import PySimpleGUI as sg
import cx_Oracle
from Add_New_Classes import do_it

con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
cur = con.cursor(scrollable=True)
classes = []
period = []
year = []
column = []

cur.execute("select * from EOM_CLASS")
for row in cur:
    classes.append(row[0])
    year.append(str(row[1]))
    period.append(str(row[2]))

for x in range(len(
        classes) - 1):  # x is a string and not a integer that represent the xth item in the array, x is literally 'ICS3U' then 'ICS4U' then...
    column.append([sg.Text(classes[x] + "     ", size=(20, 1), justification='right'),
                   sg.Button('access', button_color=('black', 'orange')), sg.Radio('select', "RADIO1")], )
    column.append([sg.Text('Period: ' + period[x]), sg.Text('Year: ' + year[x])], )

column.append([sg.Text(classes[len(classes) - 1] + "     ", size=(20, 1), justification='right'),
               sg.Button('access', button_color=('black', 'orange')), sg.Radio('select', "RADIO1", default=True)], )
column.append([sg.Text('Period: ' + period[len(classes) - 1]), sg.Text('Year: ' + year[x])])

layout = [
    [sg.Text('  Class selection', size=(17, 1), font=("Helvetica", 25), text_color='black', justification='center')],
    [sg.Column(column, scrollable=True, size=(350, 200))],
    [sg.Button('Add Class', button_color=('white', 'black'), font=("Helvetica", 15), key='key_add_class'),
     sg.Button('Edit Class', button_color=('white', 'black'), font=("Helvetica", 15), key='key_edit_class'),
     sg.Button('Delete Class', button_color=('white', 'black'), font
     =("Helvetica", 15), key='key_delete_class')]]

# event, values  = sg.Window('Class selection', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
window = sg.FlexForm('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

while True:
    event, values = window.Read()
    if event == 'key_add_class':
        do_it()

    if event is None:
        break
window.Close()