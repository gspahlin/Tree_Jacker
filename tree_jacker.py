#this is the graphical interface portion of the Tree_Jacker program
import os
import PySimpleGUI as sg
from tree_folder import Folder as tf
import time
import shutil as sht
import numpy as np

#setup the layout of the program
i_map = [
    [sg.Text('Specify Folder For Analyisis'),
    sg.In(size = (25, 1), enable_events = True, key='-FOLDER-'),
    sg.FolderBrowse() 
    ],

    [sg.Button('Set Target Folder')]

]

#create window
window = sg.Window('Tree Jacker', i_map, resizable=True)

#create event loop 
while True:
    event, values = window.read()

    if event == '-FOLDER-':
        #values['-FOLDER-'] ends up being whatever is in the sg.In box
        folder = values['-FOLDER-']

    if event == 'Set Target Folder':
        print(folder)


        #kill the program if the user hits the close box or 
    if event== sg.WIN_CLOSED:
        #this command breaks the loop
        break

#this command closes the Window that I've stored in the window variable
window.close()
