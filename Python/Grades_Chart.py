import cx_Oracle
import PySimpleGUI as sg

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

BOX_SIZE = 17

layout = [
    [sg.Graph((1800, 700), (0, 450), (450, 0), key='_GRAPH_', change_submits=True, drag_submits=False)],
]

window = sg.Window('Window Title', ).Layout(layout).Finalize()

g = window.FindElement('_GRAPH_')

for row in range(16):
    for col in range(25):
        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')


while True:  # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    mouse = values['_GRAPH_']

    if event == '_GRAPH_':
        if mouse == (None, None):
            continue
        box_x = mouse[0] // BOX_SIZE
        box_y = mouse[1] // BOX_SIZE
        print(box_x, box_y)

window.Close()
