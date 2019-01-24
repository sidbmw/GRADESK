# author: Mike Dong, Early October
# version: 6.2

import PySimpleGUI as sg
import cx_Oracle
from Add_New_Classes import run_program as add
from Edit_Classes import run_program as edit
from Grades_Chart import run_program as access


def run_program():  # the function that runs everything
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # connects to the database
    cur = con.cursor(scrollable=True)  # object, used to execute SQL commands in python
    classes = []  # list, stores the names of the classes
    period = []  # list, stores the period of the classes
    year = []  # list, stores the active year data of the classes
    column = []  # list, stores elements of the gui
    student_numbers = []  # list, stores the student numbers of the students in class that is going to be deleted

    def get_number_of_students(course_code):  # function, gets the student numbers in a given class and returns the number of students
        cur.execute("select * from EOM_STUDENTS")
        number_of = 0
        for row in cur:  # for loop that goes through the students data table
            if row[1] == course_code:  # checks if a student belongs to a certain class
                number_of += 1
                student_numbers.append(row[0])
        return number_of

    cur.execute("select * from EOM_CLASS") 
    for row in cur:  # goes through the classes data table and put the values into respective lists
        word = row[0].split('/')

        classes.append(word[0])
        year.append(str(word[1]))
        period.append(str(row[1]))

    for x in range(len(classes)):  # repeats the same amount of time as the number of classes so everything is displayed
        if x == len(classes) - 1:  # special gui elements for the last class, set the select to True
            column.append([sg.Text(classes[x] + "     ", size=(20, 1), justification='right'),
                           sg.Button('access', button_color=('black', 'orange'), key=str(x)), sg.Radio('select', "RADIO1", default=True)],
                          )
        else:
            column.append([sg.Text(classes[x] + "     ", size=(20, 1), justification='right'),
                           sg.Button('access', button_color=('black', 'orange'), key=str(x)),
                           sg.Radio('select', "RADIO1", default=True)],
                          )
        column.append([sg.Text('Period: ' + period[x]), sg.Text('Year: ' + year[x])], )
        column.append([sg.Text(' ')])

    layout = [  # where the gui is put together, each [] means that its a line's content
        [sg.Text('          Class selection', size=(17, 1), font=("Helvetica", 25), text_color='black', justification='center')],
        [sg.Column(column, scrollable=True, size=(400, 300))],
        [sg.Button('Add Class', button_color=('white', 'black'), font=("Helvetica", 15), key='key_add_class'),
         sg.Button('Edit Class', button_color=('white', 'black'), font=("Helvetica", 15), key='key_edit_class'),
         sg.Button('Delete Class', button_color=('white', 'black'), font
         =("Helvetica", 15), key='key_delete_class')]]

    window = sg.FlexForm('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)  # used to open up a window and display everything

    def reopen():  # function closes the window and opens it again, refreshing and updating the gui
        window.Close()
        run_program()

    while True:  # runs as long as the window is open, similar to an action listener
        event, values = window.Read()  # the pysimplegui equivalent of an action listener

        if event == 'key_add_class':  # checks if it was the add classes button that was pressed
            add()
            reopen()

        if event == 'key_edit_class':  # checks if it was the edit class button that was pressed
            for x in range(len(classes)):  # goes through and finds the class that has been selected
                if values[x]:
                    edit(classes[x], period[x], year[x])
                    reopen()

        if event == 'key_delete_class':  # checks if it was the delete class button that was pressed
            deleted = ''  # variable, a variable to used to hold the name of the selected class
            for x in range(len(classes)):  # goes through and finds the selected class
                if values[x]:  # check if x has been selected
                    deleted = classes[x]
                    cur.execute("DELETE FROM EOM_CLASS WHERE CLASS = :course_code", course_code=str(classes[x] + '/' + year[x]))
                    con.commit()

            cur.execute("select * from EOM_STUDENTS")
            for z in range(get_number_of_students(deleted)):  # runs as many times as it is needed to deleted all students of the selected class
                cur.execute("DELETE FROM EOM_STUDENTS WHERE STUDENT_ID = :v_id", v_id=student_numbers[x])
            reopen()

        if event is None:  # check if the window should be closed
            break

        for x in range(len(classes)):  # goes through all the access buttons
            if event == str(x):  # check if it was x that was pressed
                access(classes[x] + '/' + year[x])
                reopen()

    window.Close()


run_program()
