import PySimpleGUI as sg
import marking_first
import cx_Oracle
import sys


marking_first.do_it()
def getName(x):
    cur.execute("select * from EOM_STUDENTS")
    for row in cur:
        if x == (row[0]):
            return str(row[2] + " " + row[3])


def getRows():
    cur.execute("select * from EOM_STUDENTS")
    num_of_rows = 0
    for row in cur:
        num_of_rows += 1
    return num_of_rows


con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
cur = con.cursor(scrollable=True)
sql_rows = getRows()

mark = [[],
        []]
column = []  # part of the layout

sg.ChangeLookAndFeel('DarkBlue')


if marking_first.quit_option ==False:
    for x in range(int(marking_first.numberOfMark)):
        column.append(
            [sg.Text('Expectation  ', text_color='white', justification='left'), sg.InputText('', size=(10, 1))], )
        column.append(
            [sg.Text('Mark            ', text_color='white', justification='left'), sg.InputText('', size=(10, 1))], )
        column.append([sg.Text('_' * 100, size=(23, 1))], )

    for x in range(int(sql_rows)):
        open_variable = True
        studentID = x+1
        student_name = getName(studentID)
        layout = [[sg.Text('Mark entry - ' + student_name, size=(25, 1),
                           font=("Helvetica", 15), justification='center')],
                  [sg.Column(column, scrollable=True, size=(225, 300))],
                  [sg.Button('Save', key='key_save'),
                   sg.Button('Next Student', key='key_next_stud')]]

        window = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

        while open_variable:
            # This is the code that reads and updates your window
            event, values = window.Read()
            saved = False  #########################################################################################
            # if marking_first.quit_option == True:
            #   break
            if event == 'key_save':
                for x in range(int(marking_first.numberOfMark)):
                    tracker = int(x * 2)
                    if values[tracker + 0] != None:
                        if values[tracker + 1] != None:
                            mark[0].append(values[tracker + 0])
                            mark[1].append(values[tracker + 1])
                        else:
                            sg.Popup('incomplete input')
                    else:
                        sg.Popup('incomplete input')

                for x in range(int(marking_first.numberOfMark)):

                    cur.execute("""
                        insert into EOM_MARKS (STUDENT_ID, COLOUR, TASK, EXPECTATION, MARK, COMMENTS, ANOMALY, DELETED_FLAG)
                        values (:studentID, :color, :nameOfMark, :task_variable, :mark_variable, :null_variable, :No_variable, 
                        :No_variable_second)""",

                                task_variable=mark[0][x],
                                mark_variable=mark[1][x],
                                null_variable='',
                                studentID=studentID,
                                No_variable='N',
                                No_variable_second='N',
                                color=marking_first.color,
                                nameOfMark=marking_first.nameOfMark
                                )

                    con.commit()
                saved = True
            if event == 'key_next_stud':
                mark = [[], []]

                break

            if values is None:
                sys.exit()

        window.Close()  # Don't forget to close your window!

    sg.Popup('You have just finished marking ' + marking_first.nameOfMark + '!')