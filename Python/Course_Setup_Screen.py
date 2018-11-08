# Author: Siddharth Natamai
# Date: November 7, 2018

# !/usr/bin/env python

import PySimpleGUI as sg

layout = [[sg.Text('Add New Classes', font =("Helvetica", 25))],

]

window = sg.Window('Enter Login Credentials', default_element_size=(40, 1)).Layout(layout)


event, values = window