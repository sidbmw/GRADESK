import PySimpleGUI as sg
import marking_first
import cx_Oracle
import sys

marking_first.do_it()


def do_it(course):
    theArray = []

    def getName(x):
        cur.execute("select * from EOM_STUDENTS")
        for row in cur:
            if x == (row[0]):
                return str(row[2] + " " + row[3])


    def getRows(x):
        cur.execute("select * from EOM_STUDENTS")
        v_row = 0
        for row in cur:
            if row[1] == x:
                theArray.append(v_row)
            v_row += 1
        return v_row

    con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)

    mark = [[],
            []]

    for x in range(int(marking_first.numberOfMark)):
        mark[0].append("")
        mark[1].append("")

    column = []  # part of the layout

    sg.ChangeLookAndFeel('DarkBlue')

    for x in range(int(marking_first.numberOfMark)):
        column.append(
            [sg.Text('Expectation  ', text_color='white', justification='left'),
             sg.InputText(mark[0][x], size=(10, 1))], )
        column.append(
            [sg.Text('Mark            ', text_color='white', justification='left'),
             sg.InputText('', size=(10, 1))], )
        column.append([sg.Text('_' * 100, size=(23, 1))], )

    mark = [[], []]

    if marking_first.quit_option == False:

        for x in range(int(getRows(course))):
            open_variable = True
            studentID = int(theArray[x])+1
            student_name = getName(studentID)

            layout = [[sg.Text('Mark entry - ' + student_name, size=(25, 1),
                               font=("Helvetica", 15), justification='center')],
                      [sg.Column(column, scrollable=True, size=(225, 300), vertical_scroll_only=True)],
                      [sg.Button('Next Student', key='key_next_stud')]]

            window = sg.Window('Mark ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

            while open_variable:
                event, values = window.Read()
                saved = False
                do = False
                if event == 'key_next_stud':
                    mark = [[], []]
                    for x in range(int(marking_first.numberOfMark)):
                        tracker = int(x * 2)
                        if values[tracker + 0] is not None:
                            if values[tracker + 1] is not None:
                                print(mark)
                                mark[0].append(values[tracker + 0])
                                mark[1].append(values[tracker + 1])
                                do = True
                            else:
                                sg.Popup('incomplete input')
                                do = False
                        else:
                            sg.Popup('incomplete input')
                            do = False

                    if do:
                        for y in range(int(marking_first.numberOfMark)):
                            print(mark, y)
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

                            column = ()

                    if saved:
                        break

                if values is None:
                    sys.exit()

            window.Close()  # Don't forget to close your window!
        sg.Popup('You have just finished marking ' + marking_first.nameOfMark + '!')


do_it('ICS4U-01/2018')
