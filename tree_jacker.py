#this is the graphical interface portion of the Tree_Jacker program
import os
import PySimpleGUI as sg
from tree_folder import Folder as tf
import time
import shutil as sht
import numpy as np

#setup the layout of the program
#input section
i_map = [
    [sg.Text('Specify Folder For Analyisis'),
    sg.In(size = (25, 1), enable_events = True, key='-TFOLDER-'),
    sg.FolderBrowse()],

    [sg.Button('Set Target Folder')]

]
#specify output
o_map = [
    [sg.Text('Specify Output Folder'),
    sg.In(size = (25, 1), enable_events = True, key = '-OFOLDER-'),
    sg.FolderBrowse()], 

    [sg.Button('Set Output Folder')]
    ]

r_map = [[sg.Button('RUN')]]

#full layout
f_layout = [[sg.Column(i_map), sg.VSeparator(), sg.Column(o_map), r_map]]

#create window
window = sg.Window('Tree Jacker', f_layout, resizable=True)

#create event loop 
while True:
    event, values = window.read()

    if event == '-TFOLDER-':
        #values['-FOLDER-'] ends up being whatever is in the sg.In box
        folder = values['-TFOLDER-']
    
    #set variable folder_path using the appropriate button
    if event == 'Set Target Folder':
        print(f'Target folder set as {folder}')
        folder_path = folder

    if event== '-OFOLDER-':
        ofolder = values['-OFOLDER-']

    if event == 'Set Output Folder':
        print(f'Target folder set as {folder}')
        output_folder = ofolder

    if event == 'RUN':
        #run a tree_jack analysis
        try:
            fold = tf(folder_path)

            fold.get_sub_paths(fold.dir_path)

            fold.investigate_folder(fold.subpaths)

            #hardwire floor for now
            floor = 0

            file_info_df = fold.investigate_data_out(floor)

            file_info_df.to_csv(f'{output_folder}/folder_contents.csv', index = False)

            print(f'found {len(fold.size_list)} files')

            print(f'encountered {len(fold.errors)} errors')

            print(f'folder_contents written to {output_folder}')
        
        except:
            print('Error: make sure inputs are set and try again')


        #kill the program if the user hits the close box or 
    if event== sg.WIN_CLOSED:
        #this command breaks the loop
        break

#this command closes the Window that I've stored in the window variable
window.close()
