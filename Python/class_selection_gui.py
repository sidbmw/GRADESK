import PySimpleGUI as sg
import cx_Oracle
from Add_New_Classes import do_it as add
from Edit_Classes import do_it as edit


def do_it():
    con = cx_Oracle.connect('system/earluser@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)
    classes = []
    period = []
    year = []
    column = []

    cur.execute("select * from EOM_CLASS")
    for row in cur:
        word = row[0].split('/')

        classes.append(word[0])
        year.append(str(word[1]))
        period.append(str(row[1]))

    for x in range(len(classes) - 1):
        column.append([sg.Text(classes[x] + "     ", size=(20, 1), justification='right'),
                       sg.Button('access', button_color=('black', 'orange')), sg.Radio('select', "RADIO1")], )
        column.append([sg.Text('Period: ' + period[x]), sg.Text('Year: ' + year[x])], )
        column.append([sg.Text(' ')])

    column.append([sg.Text(classes[len(classes) - 1] + "     ", size=(20, 1), justification='right'),
                   sg.Button('access', button_color=('black', 'orange')), sg.Radio('select', "RADIO1", default=True)], )
    column.append([sg.Text('Period: ' + period[len(classes) - 1]), sg.Text('Year: ' + year[x])])

    layout = [
        [sg.Text('  Class selection', size=(17, 1), font=("Helvetica", 25), text_color='black', justification='center')],
        [sg.Column(column, scrollable=True, size=(350, 200))],
        [sg.Button('Add Class', button_color=('white', 'black'), font=("Helvetica", 15), key='key_add_class'),
         sg.Button('Edit Class', button_color=('white', 'black'), font=("Helvetica", 15), key='key_edit_class'),
         sg.Button('Delete Class', button_color=('white', 'black'), font
         =("Helvetica", 15), key='key_delete_class')]]

    # event, values  = sg.Window('Class selection', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
    window = sg.FlexForm('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    while True:
        event, values = window.Read()
        if event == 'key_add_class':
            add()

        if event == 'key_edit_class':
            for x in range(len(classes)):
                if values[x]:
                    edit(classes[x], period[x], year[x])

        if event == 'key_delete_class':
            for x in range(len(classes)):
                if values[x]:
                    cur.execute("DELETE FROM EOM_CLASS WHERE CLASS = :stuff", stuff=str(classes[x] + '/' + year[x]))

            con.commit()

        if event is None:
            break

    window.Close()


do_it()
