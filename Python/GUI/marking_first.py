import PySimpleGUI as sg


nameOfMark = ' '
numberOfMark = 1

layout = [[sg.Text('  Set up assignment', size=(17, 1), font=("Helvetica", 15), text_color='black', justification = 'center')],
        [sg.Radio('Test             ', 'RADIO1', default=True, text_color = 'red'), sg.Radio('Assignment   ', 'RADIO1', text_color = 'blue')],
        [sg.Radio('Presentation ', 'RADIO1', text_color = 'green'), sg.Radio('Quiz           ', 'RADIO1', text_color = 'Yellow')],
        [sg.Text('Name of Assigment      '), sg.InputText('', size = (10,1))],
        [sg.Text('Number of expectations'), sg.InputText('', size = (10,1))],
        [sg.Quit(button_color=('black', 'orange')), sg.Button('Next', key = 'next_key')]] #get the next key working

window = sg.FlexForm('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

while True:
    event, values = window.Read()
    if event is None:
        break
    if event == 'Quit':
        break
    if event == 'next_key': #the next key is not working for somereason
        if values[4] and values[5] != None:

            nameOfMark = values[4]
            numberOfMark = values[5]
            sg.Popup(numberOfMark)
        else:
            sg.Popup('invalid input')

window.Close()
