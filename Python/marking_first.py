import PySimpleGUI as sg
import cx_Oracle

nameOfMark = ' '
numberOfMark = 1
color = ' '
quit_option = False

def do_it():
    global nameOfMark
    global numberOfMark
    global color
    global quit_option
    con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)

    sg.ChangeLookAndFeel('DarkBlue')

    layout = [
        [sg.Text('  Set up assignment', size=(17, 1), font=("Helvetica", 15), text_color='white', justification='center')],
        [sg.Radio('Test             ', 'RADIO1', default=True, text_color='blue'),
         sg.Radio('Assignment   ', 'RADIO1', text_color='red')],
        [sg.Radio('Presentation ', 'RADIO1', text_color='green'),
         sg.Radio('Quiz           ', 'RADIO1', text_color='Yellow')],
        [sg.Text('Name of Assigment      '), sg.InputText('', size=(10, 1))],
        [sg.Text('Number of expectations'), sg.InputText('', size=(10, 1))],
        [sg.Quit(button_color=('black', 'orange')), sg.Button('Next', key='next_key')]]  # get the next key working

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
        if event == 'next_key':  # the next key is not working for some reason
            cur.execute("select * from EOM_MARKS")
            for row in cur:
                if values[4] == (row[2]):  # row[0] is row 1 first term, row 2 first term, row 3 first term...
                    sg.Popup("there's already an assignment like this")
                    break_variable = False
                    break
            if values[4] and values[5] != None:
                if values[0] == True:
                    color = 'blue'
                if values[1] == True:
                    color = 'red'
                if values[2] == True:
                    color = 'green'
                if values[3] == True:
                    color = 'yellow'
                nameOfMark = values[4]
                numberOfMark = values[5]
                if break_variable == True:
                    break
        else:
            sg.Popup('invalid input')

    window.Close()
