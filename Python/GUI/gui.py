import PySimpleGUI as sg

classes = ['ICS3U.01', 'ICS4U.01', 'MPM2C.01', 'class 4' , 'class 5' , 'class 6', 'class 7', 'class last']
column=[]
for x in classes:
    column.append([sg.Text(x + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))])


            #[sg.Text(classes[0] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))],
            #[sg.Text(classes[1] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))],
            #[sg.Text(classes[2] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))],
            #[sg.Text(classes[3] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))],
            #[sg.Text(classes[4] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))],
            #[sg.Text(classes[5] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))],
            #[sg.Text(classes[6] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))],
            #[sg.Text(classes[7] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))],
    if x == 'class 7':
        break

column.append([sg.Text(classes[len(classes) -1] + "     ", size=(20, 1), justification = 'right'), sg.Button('select', button_color =( 'black', 'orange'))])


layout = [[sg.Text('  Class selection', size=(17, 1), font=("Helvetica", 25), text_color='black', justification = 'center')],
    [sg.Column(column,scrollable=True, size=(300,200) )]]


event, values  = sg.Window('Everything bagel', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
