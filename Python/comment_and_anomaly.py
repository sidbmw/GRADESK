# author: Mike Dong, Early January
# version: 2.2

import PySimpleGUI as sg
import cx_Oracle
from input_checker import check_string
from input_checker import check_expectation
from input_checker import check_mark


def run_program(student_id, mark):  # the function that runs everything, requires student number and name of the mark to function
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # connects to the database
    cur = con.cursor(scrollable=True)  # object, used to execute SQL commands in python
    old_comments = cur.execute("select COMMENTS from EOM_MARKS where STUDENT_ID=:v_id and TASK=:v_mark",  # variable, what the comment is currently
                               v_id=student_id, v_mark=mark)
    old_comments = cur.fetchone()

    if list(str(old_comments))[0] == '<':  # if comment is blank it will show some weird SQL thing, this gets rid of it
        old_comments = ''

    layout = [[sg.Text('Comments', font=("Helvetica", 11), text_color='black', justification='left')],  # where the gui is put together, each [] means that its a line's content
              [sg.InputText(old_comments, size=(22, 0))],
              [sg.Text('      Mark as anomaly'), sg.Checkbox('')],
              [sg.Button('Delete this assignment', button_color=('black', 'orange'), key='_delete_')],
              [sg.Button('Edit', button_color=('black', 'orange'), key='_edit_'), sg.Text('            '),
               sg.Button('Save', button_color=('black', 'orange'), key='_save_')]]

    window = sg.Window('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)  # used to open up a window and display everything

    while True:   # runs as long as the window is open, similar to an action listener
        event, values = window.Read()  # the pysimplegui equivalent of an action listener
        if event is None:
            window.Close()

        if event == '_delete_':  # checks if it was the add classes button that was pressed
            cur.execute("UPDATE EOM_MARKS SET DELETED_FLAG=:v_delete WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                        v_delete='Y', v_id=student_id, v_mark=mark)
            print('1')
            con.commit()
            sg.Popup('All marks associated with ' + mark + " has been deleted")
            break

        if event == '_edit_':  # checks if it was the edit button that was pressed
            window.Close()
            edit_mark(student_id, mark)

        if event == '_save_':  # checks if it was the save classes button that was pressed
            comments = values[0]
            if check_string(comments, 'str', 250):  # check if the comment is too long
                if values[1]:  # if this is True then the mark will be marked as an anomaly
                    cur.execute("UPDATE EOM_MARKS SET COMMENTS=:v_comment, ANOMALY=:v_anomaly WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                                v_comment=comments, V_anomaly='Y', v_id=student_id, v_mark=mark)
                    con.commit()

                cur.execute("UPDATE EOM_MARKS SET COMMENTS = :v_comment WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                            v_comment=comments, v_id=student_id, v_mark=mark)
                con.commit()
            else:
                sg.Popup('Invalid comment')

        if event is None:
            break


# ----------------------------------------------------------------------------------------------------------------------


def edit_mark(student_id, mark_name):  # the function that runs everything, also require those two parameters
    def reopen():  # object, used to execute SQL commands in python
        window.Close()
        edit_mark(student_id, mark_name)

    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # connects to the database
    cur = con.cursor(scrollable=True)  # checks if changes were made
    number_of_marks = 0  # variable, how many sets of expectation/mark to display
    student_name = ''  # variable, holds the full name of the student
    column = []  # part of the layout
    mark = [[],  # empty the list before values are added into it
            []]

    cur.execute("select * from EOM_STUDENTS")
    for row in cur:  # goes through the students table
        if student_id == (row[0]):  # checks if this is the right student
            student_name = str(row[2] + " " + row[3])

    cur.execute("select * from EOM_MARKS")
    for row in cur:  # goes through marks table
        if row[0] == student_id and row[2] == mark_name:  # check if this is the mark we need
            number_of_marks += 1
            mark[0].append(row[3])
            mark[1].append(row[4])

    for z in range(int(number_of_marks)):  # runs once for every expectation/mark that is in the assessment
        column.append(
            [sg.Text('Expectation  ', text_color='black', justification='left'),
             sg.InputText(mark[0][z], size=(10, 1))], )
        column.append(
            [sg.Text('Mark            ', text_color='black', justification='left'),
             sg.InputText(mark[1][z], size=(10, 1))], )
        column.append([sg.Text('_' * 100, size=(23, 1))], )

    layout = [[sg.Text('Editing ' + mark_name + ' for ' + student_name, size=(25, 1),  # where the gui is put together, each [] means that its a line's content
                       font=("Helvetica", 15), justification='center')],
              [sg.Column(column, scrollable=True, size=(225, 300), vertical_scroll_only=True)],
              [sg.Button('Finish Marking', key='key_finish')]]

    window = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)  # used to open up a window and display everything

    while True:   # runs as long as the window is open, similar to an action listener
        event, values = window.Read()  # the pysimplegui equivalent of an action listener

        if event is None:
            window.Close()

        if event == 'key_finish':  # checks if it was the finish marking button that was pressed
            edited = 0  # variable, checks if the 
            run_sql = False  # variable, decides whether the program runs the SQL script
            saved = False  # variable, stores boolean on whether the marking has been completed
            for x in range(int(number_of_marks)):  # runs once for every expectation/mark entered
                tracker = x * 2
                if values[tracker + 1] == mark[1][x]:  # check if the mark has been changed
                    edited += 1
                if values[tracker + 0] is not None and check_expectation(values[tracker + 0]):  # check if the expectation is valid
                    if values[tracker + 1] is not None and check_mark(values[tracker + 1]):  # check if the mark is valid
                        mark[0].append(values[tracker + 0])
                        mark[1].append(values[tracker + 1])
                        run_sql = True
                    else:
                        sg.Popup('Invalid expectation')
                        run_sql = False
                else:
                    sg.Popup('Invalid mark')
                    run_sql = False
            if edited == number_of_marks:  # check if the program should or should not run the sql part
                sg.Popup('Edit an expectation or mark to save')
                reopen()

            if run_sql:  # if everything went well basically, no invalid input
                for y in range(int(number_of_marks)):  # runs once for every set of expectation and mark
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
                break

    window.Close()
    run_program(student_id, mark_name)
