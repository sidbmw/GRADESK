import PySimpleGUI as sg

classes = ['ICS3U.01', 'ICS4U.01', 'MPM2C.01', 'class 4' , 'class 5' , 'class 6', 'class 7', 'class last']
period = ['1', '2', '3', '4', '1', '2', '3', '4']
year = ['2017', '2017', '2017', '2017', '2018', '2018', '2018', '2018']
column=[]

#if len(classes) != len(period):
#sys.exit()

for x in range(len(classes)): # x is a string and not a integer that represent the xth item in the array, x is literally 'ICS3U' then 'ICS4U' then...
    column.append([sg.Text(classes[x] + "     ", size=(20, 1), justification = 'right'), sg.Button('access', button_color =( 'black', 'orange')), sg.Radio('select', "RADIO1")],)
    column.append([sg.Text('Period: ' + period[x]), sg.Text('Year: ' + year[x])],)

    if x == 'class 7': # don't go length of array -1 because x is a string not a integer
        break

column.append([sg.Text(classes[len(classes) -1] + "     ", size=(20, 1), justification = 'right'), sg.Button('access', button_color =( 'black', 'orange')), sg.Radio('select', "RADIO1", default=True)],)
column.append([sg.Text('Period: ' + period[len(classes) -1]), sg.Text('Year: ' + year[x])])

layout = [[sg.Text('  Class selection', size=(17, 1), font=("Helvetica", 25), text_color='black', justification = 'center')],
    [sg.Column(column,scrollable=True, size=(350,200) )],
    [sg.Button('Add Class', button_color = ('white', 'black'), font=("Helvetica", 15)), sg.Button('Edit Class', button_color = ('white', 'black'), font=("Helvetica", 15)), sg.Button('Delete Class', button_color = ('white', 'black'), font
    =("Helvetica", 15))]]

event, values  = sg.Window('Class selection', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()
