import cx_Oracle
import PySimpleGUI as sg

con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
cur = con.cursor(scrollable=True)

BOX_SIZE = 15

layout = [
    [sg.Graph((1800, 700), (0, 450), (450, 0), key='_GRAPH_', change_submits=True, drag_submits=False)],
]

window = sg.Window('Window Title', ).Layout(layout).Finalize()

g = window.FindElement('_GRAPH_')

student_id = 1

cur.execute("SELECT COUNT (*) FROM EOM_MAIN_SCREEN_LAYOUT WHERE STUDENT_ID = :student_id", student_id=student_id)
v_num_of_rows = cur.fetchall()
v_num_of_rows = [n[0] for n in v_num_of_rows]
print(v_num_of_rows[0])


for row in range(v_num_of_rows[0]):
    for col in range(27):
        v_table_data = cur.execute(
            """SELECT expectation, x_inc, x_r, x_1mm, x_1ms1, x_1, x_1s1p, x_1p, x_1ps2m, x_2m, x_2ms2, x_2, x_2s2p, x_2p, x_2ps3m, x_3m, x_3ms3, x_3, x_3s3p, x_3p, x_3ps4m, x_4m, x_4ms4, x_4, x_4s4p, x_4p, x_4pp FROM EOM_MAIN_SCREEN_LAYOUT WHERE STUDENT_ID = :student_id""",
            student_id=student_id)

        raw_data = cur.fetchall()
        cooked_data = [n[col] for n in raw_data]

        print(raw_data)

        if 1 <= col <= 2:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black', fill_color='red')
        if col == 3:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 4:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 5:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 6:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 7:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 8:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 9:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 10:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 11:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 12:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 13:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 14:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 15:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        if col == 16:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        else:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')

        g.DrawText('{}'.format(cooked_data[row]), (col * BOX_SIZE + 13, row * BOX_SIZE + 10))


while True:  # Event Loop
    event, values = window.Read()
    # print(event, values)
    if event is None or event == 'Exit':
        break
    mouse = values['_GRAPH_']

    if event == '_GRAPH_':
        if mouse == (None, None):
            continue
        box_x = mouse[0] // BOX_SIZE
        box_y = mouse[1] // BOX_SIZE
        # print(box_x, box_y)

window.Close()
