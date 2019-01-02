import cx_Oracle
import PySimpleGUI as sg
from mark_gui import do_it as mark  # this is for the add assignment button, mark(course code + year)


def do_it(course):
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)

    BOX_SIZE = 16

    event = ''

    # class_code = 'ICS4U-01/2018'
    class_code = course

    min_sort_id = cur.execute("SELECT MIN(SORT_ID) FROM EOM_STUDENTS WHERE CLASS = :class_code", class_code=class_code)
    min_sort_id = cur.fetchall()
    min_sort_id = [n[0] for n in min_sort_id]
    min_sort_id = min_sort_id[0]
    sort_id = min_sort_id
    # sort_id = 1

    while event != 'close_window':
        sort_id = cur.execute("select sort_id from EOM_STUDENTS where SORT_ID = :sort_id", sort_id=sort_id)
        sort_id = cur.fetchall()
        sort_id = [n[0] for n in sort_id]
        sort_id = sort_id[0]

        student_id = cur.execute("SELECT STUDENT_ID FROM EOM_STUDENTS WHERE SORT_ID = :sort_id", sort_id=sort_id)
        student_id = cur.fetchall()
        student_id = [n[0] for n in student_id]
        student_id = student_id[0]

        student_first_name = cur.execute("SELECT FIRST_NAME FROM EOM_STUDENTS WHERE STUDENT_ID = :student_id", student_id=student_id)
        student_first_name = cur.fetchall()
        student_first_name = [n[0] for n in student_first_name]
        student_first_name = student_first_name[0]

        student_last_name = cur.execute("SELECT LAST_NAME FROM EOM_STUDENTS WHERE STUDENT_ID = :student_id", student_id=student_id)
        student_last_name = cur.fetchall()
        student_last_name = [n[0] for n in student_last_name]
        student_last_name = student_last_name[0]

        student_full_name = student_last_name + str(", ") + student_first_name
        # print(student_first_name, student_last_name)

        class_code = cur.execute("SELECT CLASS FROM EOM_STUDENTS WHERE STUDENT_ID = :student_id", student_id=student_id)
        class_code = cur.fetchall()
        class_code = [n[0] for n in class_code]
        class_code = class_code[0]

        cur.callproc('eom_build_layout', [student_id])

        scrollable_column = [[sg.Graph((1800, 700), (0, 450), (450, -60), key='_GRAPH_', change_submits=True, drag_submits=False)]]

        layout = [
            [sg.Text(student_full_name, font='Helvetica', size=(40, 1)), sg.Text(class_code, font='Helvetica', size=(40, 1))],
            [sg.Column(scrollable_column, scrollable=True, size=(1800, 700), vertical_scroll_only=True)],
            [sg.Button('Previous Student', key='_prev_student_'), sg.Button('Next Student', key='_next_student_'), sg.Button("Exit", key="close_window")]
        ]

        window = sg.Window(student_full_name).Layout(layout).Finalize()

        g = window.FindElement('_GRAPH_')

        cur.execute("SELECT COUNT (*) FROM EOM_MAIN_SCREEN_LAYOUT WHERE STUDENT_ID = :student_id", student_id=student_id)
        v_num_of_rows = cur.fetchall()
        v_num_of_rows = [n[0] for n in v_num_of_rows]

        # print(v_num_of_rows[0])

        for row in range(v_num_of_rows[0]):
            for col in range(27):

                if row == 0:
                    arr_marks = ['Expectation', 'INC', 'R', '1--', '1-/1', '1', '1/1+', '1+', '1+/2-', '2-', '2-/2', '2', '2/2+', '2+', '2+/3-', '3-', '3-/3', '3',
                                 '3/3+',
                                 '3+', '3+/4-', '4-', '4-/4', '4', '4/4+', '4+', '4++']
                    g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black',
                                    fill_color='#2196F3')
                    g.DrawText('{}'.format(arr_marks[col]), (col * BOX_SIZE + 13, row * BOX_SIZE + 10))

                else:
                    v_table_data = cur.execute(
                        """SELECT expectation, x_inc, x_r, x_1mm, x_1ms1, x_1, x_1s1p, x_1p, x_1ps2m, x_2m, x_2ms2, x_2, x_2s2p, x_2p, x_2ps3m, x_3m, x_3ms3, x_3, x_3s3p, x_3p, x_3ps4m, x_4m, x_4ms4, x_4, x_4s4p, x_4p, x_4pp FROM EOM_MAIN_SCREEN_LAYOUT WHERE STUDENT_ID = :student_id""",
                        student_id=student_id)
                    raw_data = cur.fetchall()
                    cooked_data = [n[col] for n in raw_data]
                    cooked_data = ['' if v is None else v for v in cooked_data]

                    # print(raw_data)

                    if 1 <= col <= 2:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black',
                                        fill_color='#F44336')
                    if 3 <= col <= 7:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black',
                                        fill_color='#E040FB')
                    if 8 <= col <= 13:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black',
                                        fill_color='#76FF03')
                    if 14 <= col <= 19:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black',
                                        fill_color='#FF8A65')
                    else:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')

                    g.DrawText('{}'.format(cooked_data[row]), (col * BOX_SIZE + 13, row * BOX_SIZE + 10))

        while True:  # Event Loop
            event, values = window.Read()
            # print(event, values)
            if event is None or event == 'Exit':
                window.Close()
                break
            mouse = values['_GRAPH_']

            if event == '_GRAPH_':
                if mouse == (None, None):
                    continue
                box_x = mouse[0] // BOX_SIZE
                box_y = mouse[1] // BOX_SIZE
                print(box_x, box_y)

            if event == '_next_student_':
                max_sort_id = cur.execute("SELECT MAX(SORT_ID) FROM EOM_STUDENTS WHERE CLASS = :class_code", class_code=class_code)
                max_sort_id = cur.fetchall()
                max_sort_id = [n[0] for n in max_sort_id]
                max_sort_id = max_sort_id[0]

                if sort_id < max_sort_id:
                    sort_id += 1
                    window.Close()
                    break
                else:
                    sg.Popup("No students after this")

            if event == '_prev_student_':
                if sort_id == min_sort_id:
                    sg.Popup("No students before this")
                else:
                    sort_id -= 1
                    window.Close()
                    break

            if event == "close_window":
                window.Close()
                break

        window.Close()
