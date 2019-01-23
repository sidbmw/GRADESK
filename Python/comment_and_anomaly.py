import PySimpleGUI as sg
import cx_Oracle
from input_checker import check_string
from input_checker import check_expectation
from input_checker import check_mark


def run_program(student_id, mark):

    def reopen():
        window.Close()
        run_program(student_id, mark)

    con = cx_Oracle.connect('system/EOM@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)
    cur.execute("select COMMENTS from EOM_MARKS where STUDENT_ID=:v_id and TASK=:v_mark",
                v_id=student_id, v_mark=mark)
    old_comments = str(cur.fetchone())
    old_comments = old_comments[2:][:len(old_comments)-5]

    layout = [[sg.Text('Comments', font=("Helvetica", 11), text_color='black', justification='left')],
              [sg.InputText(old_comments, size=(22, 0))],
              [sg.Text('      Mark as anomaly'), sg.Checkbox('')],
              [sg.Button('Delete this assignment', button_color=('black', 'orange'), key='_delete_')],
              [sg.Button('Edit', button_color=('black', 'orange'), key='_edit_'), sg.Text('            '),
               sg.Button('Save', button_color=('black', 'orange'), key='_save_')]]

    window = sg.Window('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    while True:

        event, values = window.Read()
        if event is None:
            window.Close()

        if event == '_delete_':
            cur.execute("UPDATE EOM_MARKS SET DELETED_FLAG=:v_delete WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                        v_delete='Y', v_id=student_id, v_mark=mark)
            print('1')
            con.commit()
            sg.Popup('All marks associated with ' + mark + " has been deleted")
            break

        if event == '_edit_':
            window.Close()
            edit_mark(student_id, mark)

        if event == '_save_':
            comments = values[0]
            if check_string(comments, 'str', 250):
                if values[1]:  # anomaly
                    cur.execute("UPDATE EOM_MARKS SET COMMENTS=:v_comment, ANOMALY=:v_anomaly WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                                v_comment=comments, V_anomaly='Y', v_id=student_id, v_mark=mark)
                    con.commit()

                cur.execute("UPDATE EOM_MARKS SET COMMENTS = :v_comment WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                            v_comment=comments, v_id=student_id, v_mark=mark)
                con.commit()

                reopen()
            else:
                sg.Popup('Invalid comment')

        if event is None:
            break


# ----------------------------------------------------------------------------------------------------------------------


def edit_mark(student_id, mark_name):
    def reopen():
        window.Close()
        edit_mark(student_id, mark_name)

    con = cx_Oracle.connect('system/EOM@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)
    number_of_marks = 0
    student_name = ''
    column = []  # part of the layout
    mark = [[],
            []]

    cur.execute("select * from EOM_STUDENTS")
    for row in cur:
        if student_id == (row[0]):
            student_name = str(row[2] + " " + row[3])

    cur.execute("select * from EOM_MARKS")
    for row in cur:
        if row[0] == student_id and row[2] == mark_name:
            number_of_marks += 1
            mark[0].append(row[3])
            mark[1].append(row[4])

    for z in range(int(number_of_marks)):
        column.append(
            [sg.Text('Expectation  ', text_color='black', justification='left'),
             sg.InputText(mark[0][z], size=(10, 1))], )
        column.append(
            [sg.Text('Mark            ', text_color='black', justification='left'),
             sg.InputText(mark[1][z], size=(10, 1))], )
        column.append([sg.Text('_' * 100, size=(23, 1))], )

    layout = [[sg.Text('Editing ' + mark_name + ' for ' + student_name, size=(25, 1),
                       font=("Helvetica", 15), justification='center')],
              [sg.Column(column, scrollable=True, size=(225, 300), vertical_scroll_only=True)],
              [sg.Button('Finish Marking', key='key_finish')]]

    window = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    while True:
        event, values = window.Read()

        if event is None:
            window.Close()

        if event == 'key_finish':
            edited = 0
            do = False
            saved = False
            for x in range(int(number_of_marks)):
                tracker = x * 2
                if values[tracker + 1] == mark[1][x]:
                    edited += 1
                if values[tracker + 0] is not None and check_expectation(values[tracker + 0]):
                    if values[tracker + 1] is not None and check_mark(values[tracker + 1]):
                        mark[0].append(values[tracker + 0])
                        mark[1].append(values[tracker + 1])
                        do = True
                    else:
                        sg.Popup('Invalid expectation')
                        do = False
                else:
                    sg.Popup('Invalid mark')
                    do = False
            if edited == number_of_marks:
                sg.Popup('Edit an expectation or mark to save')
                reopen()

            if do:
                print('do is True')
                for y in range(int(number_of_marks)):
                    print(mark[0][y], mark[1][y], student_id, mark_name)
                    sql_expectation = mark[0][y]
                    sql_mark = mark[1][y]
                    cur.execute("UPDATE EOM_MARKS SET EXPECTATION = :new_expectation, MARK = :new_mark "
                                "WHERE STUDENT_ID = :student_number AND TASK = :v_task "
                                "AND EXPECTATION = :old_expectation AND MARK = :old_mark",
                                new_expectation=values[y * 2],
                                new_mark=values[(y * 2) + 1],
                                student_number=student_id,
                                v_task=mark_name,
                                old_expectation=sql_expectation,
                                old_mark=sql_mark
                                )

                    con.commit()
                    saved = True

            if saved:
                print('saved is true')
                break
    window.Close()
    print('restarting cycle')
    run_program(student_id, mark_name)
