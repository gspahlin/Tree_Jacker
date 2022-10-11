#this is the graphical interface portion of the Tree_Jacker program
import PySimpleGUI as sg
from tree_folder import Folder as tf
import pandas as pd


#setup the layout of the program
#input section
i_map = [
    [sg.Text('Specify Folder For Analyisis'),
    sg.In(size = (25, 1), enable_events = True, key='-TFOLDER-'),
    sg.FolderBrowse()],

    [sg.Button('Set Target Folder')]]
#specify output
o_map = [
    [sg.Text('Specify Output Folder', justification='r'),
    sg.In(size = (25, 1), enable_events = True, key = '-OFOLDER-'),
    sg.FolderBrowse()], 

    [sg.Button('Set Output Folder')]]

#specify analysis floor

floor_map = [[sg.Text('Ignore Files Smaller Than'), sg.In(size= (5, 1), enable_events = True, key = '-FL-'), 
    sg.Text('MB')],

    [sg.Button('Set Floor')]]

#floor set to zero by default
floor = 0

#optional inputs frame
frame_l = [[sg.Checkbox('Subfolder Size Analysis', default = False, key = '-SUB-')],
    [sg.Checkbox('Storage Use By File Type', default = False, key = '-BRK-')],
    [sg.Checkbox('Duplicate Analysis', default = False, key = '-DUP-')]] 

opt_frame = [sg.Frame(layout = frame_l, title = 'Optional Analyses') ]

#optional unpack frame
unpack_l = [[sg.Text('Copy Files in Analysis Folder To'), 
    sg.In(size = (25, 1), enable_events = True, key = '-UFOLDER-'),
    sg.FolderBrowse()], 
    [sg.Button('Set Unpack Folder')],
    [sg.Checkbox('Enable (copy all files in analysis folder to specified folder)', default=False, key = '-UPK-')]]

unpack_frame = [sg.Frame(layout = unpack_l, title = 'Optional Unpack Operation')]

r_map = [[sg.Button('RUN')]]

#full layout
f_layout = [[i_map, o_map, floor_map, opt_frame, unpack_frame, r_map]]

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
        try:
            folder_path = folder
            print(f'Target folder set as {folder}')

        except:
            print('Please Select a Target Folder')
        

    if event== '-OFOLDER-':
        ofolder = values['-OFOLDER-']

    if event == 'Set Output Folder':
        try:
            output_folder = ofolder
            print(f'Output folder set as {ofolder}')
        except:
            print('Please Select an Output Folder')

    if event == '-FL-':
        fl = values['-FL-']

    if event == 'Set Floor':
        try:
            floor = fl
            print(f'Analysis Floor set to {floor} megabytes')
        except:
            print('Please specify a floor value')

    if event == '-UFOLDER-':
        ufolder = values['-UFOLDER-']

    if event == 'Set Unpack Folder':
        try:
            user_dest = ufolder
            print(f'Unpack Folder set as {ufolder}')
        except:
            print('Please Select an Unpack Folder')
        

    if event == 'RUN':
        #run a tree_jack analysis
        try:
            fold = tf(folder_path)

            fold.get_sub_paths(fold.dir_path)

            fold.investigate_folder(fold.subpaths)

            file_info_df = fold.investigate_data_out(floor)

            file_info_df.to_csv(f'{output_folder}/folder_contents.csv', index = False)

            print(f'found {len(fold.size_list)} files')

            print(f'encountered {len(fold.errors)} errors')

            print(f'folder_contents written to {output_folder}')

            if values['-SUB-']== True:
                fldr = file_info_df[['sub_folder', 'size']].copy()

                fldr_sz_info = tf.size_anal(fldr, 'sub_folder')

                fldr_sz_info.to_csv(f'{output_folder}/subfolder_size.csv', index = True)

                print(f'subfolder size analysis written to {output_folder}')

            if values['-BRK-'] == True:
                fldr2 = file_info_df[['sub_folder', 'extension', 'size']].copy()

                fldr_info2 = fldr2.groupby(['sub_folder', 'extension']).agg({'size':['count', 'sum']})

                fldr_info2.columns = ['file_count', 'total_size_mb']

                fldr_info2.to_csv(f'{output_folder}/subfolder_ext.csv', index = True)

                print(f'File Extension Breakdown written to {output_folder}')

            if values['-DUP-'] == True:
                fldr3 = file_info_df[['file_name', 'size', 'created']].copy()

                fldr_info3 = fldr3.groupby(['file_name', 'size']).agg({'created':['count']})

                #rename "created"
                fldr_info3.columns = ['copies']

                #filter dataframe
                fldr_info3 = fldr_info3[fldr_info3['copies'] > 1] 

                if len(fldr_info3) > 0:

                    #merge in paths from the original data
                    paths_df = file_info_df[['file_name', 'full_file_path']].copy()

                    #do the merge step
                    merge_df = pd.merge(fldr_info3, paths_df, on = 'file_name', how = 'inner')

                    merge_df.to_csv(f'{output_folder}/suspected_duplicates.csv', index = True)

                    print(f'duplicates analysis written to {output_folder}/suspected_duplicates.csv')
       
                else: 
                    print('No suspected duplicates found')

            if values['-UPK-'] == True:
                
                fold.move_files(fold.file_names, fold.file_path_list, user_dest)
        
        except:
            print('Error: make sure all needed inputs are set and try again')

        
        #kill the program if the user hits the close box or 
    if event== sg.WIN_CLOSED:
        #this command breaks the loop
        break

#this command closes the Window that I've stored in the window variable
window.close()
