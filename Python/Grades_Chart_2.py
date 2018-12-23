import cx_Oracle
import PySimpleGUI as sg

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

number_Of_Students = sg.PopupGetText("Number of Students")
scrollable_column = [[g.DrawLine]]

for x in range(int(number_Of_Students) - 1):
    scrollable_column = scrollable_column + [[sg.Input(), sg.Input(), sg.Button(button_text=" X ")]]
    # print(x)

layout = [[sg.Column(scrollable_column, scrollable=True, size=(1500, 700), vertical_scroll_only=True)],
          [sg.Graph((1800, 700), (0, 450), (450, 0), key='_GRAPH_', change_submits=True, drag_submits=False)]
          ]

window = sg.Window('Window Title', ).Layout(layout).Finalize()
g = window.FindElement('_GRAPH_')
window = sg.Window('Add New Courses', default_element_size=(40, 2)).Layout(layout)

while 'key_add_students':
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

window.Close()
