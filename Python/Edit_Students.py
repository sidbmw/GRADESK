# author: Mike Dong, late November
# version: 1.3

import cx_Oracle
import PySimpleGUI as sg
from Add_Students import run_program as add


def run_program(course):  # the function that runs everything, takes in the course name (name and year)
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')  # connects to the database
    cur = con.cursor(scrollable=True)  # object, used to execute SQL commands in python

    student_numbers = []  # list, stores the student numbers of the students in class that is going to be deleted

    def get_first_name(student_id):  # function, gets the student first name from the database using the student number
        cur.execute("select * from EOM_STUDENTS")
        for row in cur:  # goes through students data table
            if student_id == (row[0]):  # checks if the student number matches
                return row[2]

    def get_last_name(student_id):  # function, gets the student last name from the database using the student number
        cur.execute("select * from EOM_STUDENTS")
        for row in cur:  # goes through students data table
            if student_id == (row[0]):  # checks if the student number matches
                return row[3]

    def get_number(course_code):  # both fills the array with student ids and gets the amount of students
        cur.execute("select * from EOM_STUDENTS")
        v_row = 0
        for row in cur:  # goes through students data table
            if row[1] == course_code:  # checks if the student is in the given class
                v_row += 1
                student_numbers.append(row[0])
        return v_row

    number_of_students = get_number(course)  # variable, stores the number of students

    scrollable_column = []  # list, stores elements of the gui

    for x in range(int(number_of_students)):  # add one set of text boxes for every student in that class
        scrollable_column = scrollable_column + [[sg.Input(get_first_name(student_numbers[x])),
                                                  sg.Input(get_last_name(student_numbers[x])),
                                                  sg.Checkbox('')]]

    layout = [[sg.Stretch(), sg.Text('Edit Students', font=("Helvetica", 25)), sg.Stretch()],  # where the gui is put together, each [] means that its a line's content
              [sg.Text("                              First Name"), sg.Text("                                         "
                                                                            "             Last Name"),
               sg.Text("                          Delete")],
              [sg.Column(scrollable_column, scrollable=True, size=(650, 500), vertical_scroll_only=True)],

              [sg.Stretch(), sg.Button('Add Students', key='key_add_students', size=(20, 2)),
               sg.Button('Save', key='save_key', size=(20, 2)),
               # sg.Text("Save occurs only once 'Add Student' button is pressed"),
               sg.Stretch()]
              ]

    window = sg.Window('Edit students', default_element_size=(40, 2)).Layout(layout)  # used to open up a window and display everything

    def reopen():  # function closes the window and opens it again, refreshing and updating the gui
        window.Close()
        run_program(course)

    while True:   # runs as long as the window is open, similar to an action listener
        event, values = window.Read()  # the pysimplegui equivalent of an action listener
        if event is None or event == 'Exit':
            break

        if event == 'key_add_students':  # checks if it was the add students button that was pressed
            add(course)
            reopen()

        if event == 'save_key':  # checks if it was the save button that was pressed
            for x in range(int(number_of_students) - 1):  # runs it once for every student
                edited = False  # variable, tells the program to continue to save or not
                v_pos = x * 3
                student_first_name = values[v_pos + 2]
                student_last_name = values[v_pos + 3]

                if values[v_pos + 4]:  # check if this student is flagged for deletion
                    cur.execute("DELETE FROM EOM_STUDENTS WHERE STUDENT_ID = :v_id", v_id=student_numbers[x])
                    con.commit()
                else:
                    if student_first_name != get_first_name(student_numbers[x]):  # checks if changes were made
                        edited = True
                    if student_last_name != get_last_name(student_numbers[x]):  # checks if changes were made
                        edited = True

                    if edited:  # only run the SQL script if changes were made
                        number = int(student_numbers[x])  # the student number, SQL does not allow lists

                        cur.execute("UPDATE EOM_STUDENTS SET FIRST_NAME = :first_name, LAST_NAME = :last_name "
                                    "WHERE STUDENT_ID = :student_number",
                                    first_name=student_first_name,
                                    last_name=student_last_name,
                                    student_number=number
                                    )
                        cur.callproc('eom_student_sort')
                        con.commit()
            sg.Popup("Student names have been edited")
            cur.callproc('eom_student_sort')
            con.commit()
            reopen()

    window.Close()
