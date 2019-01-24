# author: Mike Dong, Late October
# version: 5.2

import PySimpleGUI as sg
import marking_first
import cx_Oracle
import sys
from input_checker import check_expectation
from input_checker import check_mark


def run_program(course):  # the function that runs everything, requires course to run (class + year)
    marking_first.run_program(course, 'other stuff')  # first run marking_first to get several important inputs 

    student_numbers = []  # list, the student_numbers of the students in the given class

    mark = [[],   # 2D list, stores expectation in [0] and marks in [1]
            []]

    column = []  # list, holds various elements of the gui

    def get_name(x):  # function, get the full name of a student using student number
        cur.execute("select * from EOM_STUDENTS")
        for row in cur:  # goes through the students table
            if x == (row[0]):  # checks if this student has is same student number as what is given
                return str(row[2] + " " + row[3])

    def get_number(x):  # function, get the amount of students and fill the student_numbers array
        cur.execute("select * from EOM_STUDENTS")
        v_row = 0
        for row in cur:  # goes through the students table
            if row[1] == x:  # check if this student is in the given class
                v_row += 1
                student_numbers.append(row[0])

        return v_row

    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # connects to the database
    cur = con.cursor(scrollable=True)  # object, used to execute SQL commands in python

    for x in range(int(marking_first.numberOfMark)):  # runs once for every mark that needs to be inputted
        mark[0].append("")
        mark[1].append("")

    if not marking_first.quit_option:  # if the user selected quit on the interface before this, this prevents the gui from popping up

        for x in range(int(get_number(course))):  # runs once for every student in the class, note this basically relaunches the whole program
            studentID = int(student_numbers[x])
            student_name = get_name(studentID)

            for z in range(int(marking_first.numberOfMark)):  # adds one set of text boxes for every set of expectation/mark
                column.append(
                    [sg.Text('Expectation  ', text_color='black', justification='left'),
                     sg.InputText(mark[0][z], size=(10, 1))], )
                column.append(
                    [sg.Text('Mark            ', text_color='black', justification='left'),
                     sg.InputText('', size=(10, 1))], )
                column.append([sg.Text('_' * 100, size=(23, 1))], )

            mark = [[], []]  # empty the list before values are added into it

            layout = [[sg.Text('Mark entry - ' + student_name, size=(25, 1),  # where the gui is put together, each [] means that its a line's content
                               font=("Helvetica", 15), justification='center')],
                      [sg.Column(column, scrollable=True, size=(225, 300), vertical_scroll_only=True)],
                      [sg.Button('Next Student', key='key_next_stud')]]

            window = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)  # used to open up a window and display everything

            while True:  # runs as long as the window is open, similar to an action listener
                event, values = window.Read()  # the pysimplegui equivalent of an action listener
                saved = False  # variable, stores boolean on whether the marking has been completed
                run_sql = False  # variable, decides whether the program runs the SQL script
                if event == 'key_next_stud':  # checks if it was the next student button that was pressed
                    for y in range(int(marking_first.numberOfMark)):  # runs once for everything set of expectation or mark so they can be added into the database
                        tracker = int(y * 2)
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

                    if run_sql:  # if everything went well basically, no invalid input
                        for y in range(int(marking_first.numberOfMark)):  # runs once for every set of expectation and mark
                            cur.execute("""
                                insert into EOM_MARKS (STUDENT_ID, COLOUR, TASK, EXPECTATION, MARK, COMMENTS, ANOMALY, DELETED_FLAG)
                                values (:studentID, :color, :nameOfMark, :task_variable, :mark_variable, :null_variable,
                                :No_variable, :No_variable_second)""",

                                        task_variable=mark[0][y],
                                        mark_variable=mark[1][y],
                                        null_variable='',
                                        studentID=studentID,
                                        No_variable='N',
                                        No_variable_second='N',
                                        color=marking_first.color,
                                        nameOfMark=marking_first.nameOfMark
                                        )

                            con.commit()
                            saved = True

                            column = []

                    if saved:  # if the expectations and marks have been added to database then this program can close, else it will have to keep at it until marks get added to the database
                        break

                if values is None:
                    sys.exit()

            window.Close()
        sg.Popup('You have just finished marking ' + marking_first.nameOfMark + ' for ' + course + "!")
