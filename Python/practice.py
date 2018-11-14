import PySimpleGUI as sg

gui_rows = [[sg.Text('Robotics Remote Control')],
            [sg.T(' '  * 10), sg.RealtimeButton('Forward')],
            [sg.RealtimeButton('Left'), sg.T(' '  * 15), sg.RealtimeButton('Right')],
            [sg.T(' '  * 10), sg.RealtimeButton('Reverse')],
            [sg.T('')],
            [sg.Quit(button_color=('black', 'orange'))]
            ]

window = sg.Window('Robotics Remote Control', auto_size_text=True).Layout(gui_rows)

#
# Some place later in your code...
# You need to perform a Read or Refresh call on your window every now and then or
# else it will apprear as if the program has locked up.
#
# your program's main loop
while (True):
    # This is the code that reads and updates your window
    event, values = window.Read(timeout=0)
    if event is not None:
        print(event)
    if event == 'Quit'  or values is None:
        break

window.Close()  # Don't forget to close your window!
