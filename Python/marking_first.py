import PySimpleGUI as sg
import cx_Oracle
from input_checker import check_string
from input_checker import check_expectation
from input_checker import check_mark


def do_it(course):
    global nameOfMark
    global numberOfMark
    global color
    global quit_option

    nameOfMark = ' '
    numberOfMark = 0
    color = ' '
    quit_option = False

    def get_first_student(x):
        cur.execute("select * from EOM_STUDENTS")
        for row in cur:
            if row[1] == x:
                return row[0]

    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)
    # sg.ChangeLookAndFeel('DarkBlue')

    layout = [
        [sg.Text('  Set up assignment', size=(17, 1), font=("Helvetica", 15), text_color='white', justification='center')],
        [sg.Radio('Test             ', 'RADIO1', default=True, text_color='blue'), sg.Radio('Assignment   ', 'RADIO1', text_color='red')],
        [sg.Radio('Presentation ', 'RADIO1', text_color='green'), sg.Radio('Quiz           ', 'RADIO1', text_color='Yellow')],
        [sg.Text('Name of Assigment      '), sg.InputText('', size=(10, 1))],
        [sg.Text('Number of expectations'), sg.InputText('', size=(10, 1))],
        [sg.Quit(button_color=('black', 'orange')), sg.Button('Next', key='next_key')]]

    window = sg.FlexForm('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    while True:
        event, values = window.Read()
        break_variable = True

        if event is None:
            quit_option = True
            break
        if event == 'Quit':
            quit_option = True
            break
        if event == 'next_key':
            print("im done")

            cur.execute("SELECT STUDENT_ID, TASK FROM EOM_MARKS")  # -------------------------------------------change
            fetched_data = cur.fetchall()
            student_id = [n[0] for n in fetched_data]
            task = [n[1] for n in fetched_data]

            for x in range(len(student_id)):
                if get_first_student(course) == int(student_id[x]):
                    if values[4] == task[x]:
                        sg.Popup("There's already an assignment like this for " + course + "!")
                        break_variable = False

                        break

            if values[4] and values[5] is not None:
                if values[0]:
                    color = 'blue'

                if values[1]:
                    color = 'red'

                if values[2]:
                    color = 'green'

                if values[3]:
                    color = 'yellow'

                nameOfMark = values[4]
                numberOfMark = values[5]

                if break_variable:
                    break
        else:
            sg.Popup('invalid input')


