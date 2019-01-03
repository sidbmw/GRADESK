import cx_Oracle

import PySimpleGUI as sg


def do_it(course):
    sg.ChangeLookAndFeel('DarkBlue')

    con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)

    student_numbers = []

    def get_first_name(student_id):
        cur.execute("select * from EOM_STUDENTS")
        for row in cur:
            if student_id == (row[0]):
                return row[2]

    def get_last_name(student_id):
        cur.execute("select * from EOM_STUDENTS")
        for row in cur:
            if student_id == (row[0]):
                return row[3]

    def get_rows(course_code):  # both fills the array with student ids and gets the amount of students

        cur.execute("select * from EOM_STUDENTS")
        v_row = 0
        for row in cur:
            if row[1] == course_code:
                v_row += 1
                student_numbers.append(row[0])

        return v_row

    number_of_students = get_rows('ICS4U-01/2018')  # the array is filled as well

    scrollable_column = []

    for x in range(int(number_of_students) - 1):
        scrollable_column = scrollable_column + [[sg.Input(get_first_name(student_numbers[x])),
                                                  sg.Input(get_last_name(student_numbers[x])),
                                                  sg.Checkbox('', key=x)]]

    layout = [[sg.Stretch(), sg.Text('Add Students', font=("Helvetica", 25)), sg.Stretch()],
              [sg.Text("                              First Name"), sg.Text("                                         "
                                                                            "             Last Name"),
               sg.Text("                          Delete")],
              [sg.Column(scrollable_column, scrollable=True, size=(650, 500), vertical_scroll_only=True)],

              [sg.Stretch(), sg.Button('Add Students', key='key_add_students', size=(20, 2)),
               sg.Button('Save', key='save_key', size=(20, 2)),
               # sg.Text("Save occurs only once 'Add Student' button is pressed"),
               sg.Stretch()]
              ]

    window = sg.Window('Edit students', default_element_size=(40, 2)).Layout(layout)

    reopen = False

    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break

        if event == 'save_key':
            for x in range(int(number_of_students)-1):
                edited = False
                v_pos = x * 2

                student_first_name = values[v_pos]
                student_last_name = values[v_pos + 1]

                if student_first_name != get_first_name(student_numbers[x]):
                    edited = True
                if student_last_name != get_last_name(student_numbers[x]):
                    edited = True

                # Note: Correct class must be fetched, set outside for loop and inserted into SQL query below!
                if edited:
                    cur.execute("UPDATE EOM_STUDENTS SET FIRST_NAME = :first_name AND LAST_NAME = :last_name "
                                "WHERE STUDENT_ID = :student_id",
                                firs_name=student_first_name,
                                last_name=student_last_name,
                                student_id=student_numbers[x]
                                )

        con.commit()
        sg.Popup("Student names have been stored in database")
        break

    window.Close()


#do_it('ICS4U-01/2018')
