import cx_Oracle
import PySimpleGUI as sg
import os

from mark_decide import run_program as marking_program  # this is for the add assignment button, mark(course code + year)
from comment_and_anomaly import run_program as comment_program


def run_program(course):
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # Connecting to the database with a hardcoded username and password
    cur = con.cursor(scrollable=True)

    BOX_SIZE = 23  # This sets the size of each cell in the grades_chart window. Increase or decrease this number depending on preference

    event = ''
    class_code = course  # This sets the the class_code variable to the value passed on from the class_selection_gui window

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

        student_first_name = cur.execute("SELECT FIRST_NAME FROM EOM_STUDENTS WHERE STUDENT_ID = :student_id",
                                         student_id=student_id)
        student_first_name = cur.fetchall()
        student_first_name = [n[0] for n in student_first_name]
        student_first_name = student_first_name[0]

        student_last_name = cur.execute("SELECT LAST_NAME FROM EOM_STUDENTS WHERE STUDENT_ID = :student_id",
                                        student_id=student_id)
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

        scrollable_column = [
            [sg.Graph((1800, 700), (0, 450), (450, -60), key='_GRAPH_', change_submits=True, drag_submits=False)]]

        layout = [
            [sg.Text(student_full_name, font='Helvetica', size=(40, 1)),
             sg.Text(class_code, font='Helvetica', size=(40, 1))],
            [sg.Column(scrollable_column, scrollable=True, size=(1800, 700), vertical_scroll_only=True)],
            [sg.Button('Previous Student', key='_prev_student_'), sg.Button('Next Student', key='_next_student_'),
             sg.Button("Print Report", key='_print_'), sg.Button("Add assignment", key='_add_assignment_'),
             sg.Button("Exit", key="close_window")]
        ]

        window = sg.Window(student_full_name).Layout(layout).Finalize()

        g = window.FindElement('_GRAPH_')

        cur.execute("SELECT COUNT (*) FROM EOM_MAIN_SCREEN_LAYOUT WHERE STUDENT_ID = :student_id",
                    student_id=student_id)
        v_num_of_rows = cur.fetchall()
        v_num_of_rows = [n[0] for n in v_num_of_rows]

        # print(v_num_of_rows[0])

        for row in range(v_num_of_rows[0] + 1):
            for col in range(19):

                if row == 0:
                    arr_marks = ['Expectation', 'INC', 'R', '1-', '1', '1+', '2-', '2', '2+', '3-', '3', '3+', '3+/4-', '4-', '4-/4', '4', '4/4+',
                                 '4+',
                                 '4++']
                    g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                    (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black',
                                    fill_color='#90A4AE')
                    g.DrawText('{}'.format(arr_marks[col]), (col * BOX_SIZE + 13, row * BOX_SIZE + 10))

                else:
                    v_table_data = cur.execute(
                        """SELECT expectation, x_inc, x_r, x_1m, x_1, x_1p, x_2m, x_2, x_2p, x_3m, x_3, x_3p, x_3ps4m, x_4m, x_4ms4, x_4, x_4s4p, x_4p, x_4pp FROM EOM_MAIN_SCREEN_LAYOUT WHERE STUDENT_ID = :student_id ORDER BY EXPECTATION""",
                        student_id=student_id)
                    raw_data = cur.fetchall()
                    cooked_data = [n[col] for n in raw_data]
                    cooked_data = ['' if v is None else v for v in cooked_data]
                    # print(cooked_data)

                    if 1 <= col <= 2:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                        (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3),
                                        line_color='black',
                                        fill_color='#EF5350')
                    if 3 <= col <= 5:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                        (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3),
                                        line_color='black',
                                        fill_color='#29B6F6')
                    if 6 <= col <= 8:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                        (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3),
                                        line_color='black',
                                        fill_color='#FFEE58')
                    if 9 <= col <= 12:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                        (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3),
                                        line_color='black',
                                        fill_color='#FF8A65')
                    if 13 <= col <= 19:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                        (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3),
                                        line_color='black', fill_color='#66BB6A')
                    else:
                        g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3),
                                        (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3),
                                        line_color='black')

                    g.DrawText('{}'.format(cooked_data[row - 1]), (col * BOX_SIZE + 13, row * BOX_SIZE + 10))

        while True:  # Event Loop
            event, values = window.Read()
            # print(event, values)
            if event is None or event == 'Exit':
                # print("Exited window?")
                cur.execute("delete eom_main_screen_layout")
                window.Close()
                break
            mouse = values['_GRAPH_']

            if event == '_GRAPH_':
                if mouse == (None, None):
                    continue
                box_x = mouse[0] // BOX_SIZE
                box_y = mouse[1] // BOX_SIZE
                # print(box_x, box_y)

                v_selected_mark = raw_data[box_y - 1][box_x]
                # print(raw_data[box_y - 1][box_x])
                comment_program(student_id, v_selected_mark)

            if event == '_next_student_':
                cur.execute("delete eom_main_screen_layout")
                max_sort_id = cur.execute("SELECT MAX(SORT_ID) FROM EOM_STUDENTS WHERE CLASS = :class_code",
                                          class_code=class_code)
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
                cur.execute("delete eom_main_screen_layout")
                if sort_id == min_sort_id:
                    sg.Popup("No students before this")
                else:
                    sort_id -= 1
                    window.Close()
                    break

            if event == "close_window":
                # print("closed window?")
                cur.execute("delete EOM_MAIN_SCREEN_LAYOUT")
                con.commit()
                window.Close()
                break

            if event == "_print_":
                os.environ['ORACLE_HOME'] = "C:/oraclexe/app/oracle/product/11.2.0/server"
                os.system(
                    "C:/oraclexe/app/oracle/product/11.2.0/server/bin/sqlplus.exe EOM/EOM @C:/Users/gordr/Documents/Github/ICS4U/SQL/html.sql")
                os.startfile(filepath='C:/Users/gordr/Documents/Github/ICS4U/Reports/report.htm')

            if event == '_add_assignment_':
                marking_program(class_code, student_id)

    window.Close()
