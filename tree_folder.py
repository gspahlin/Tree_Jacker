#import dependancies
import os
import numpy as np
import pandas as pd
import time
import shutil as sht

#class for working with directory trees
#this class holds data on the folder of interest, and contains methods to dump the data onto a pd dataframe
#it also has a method to use that data to move files to a user designated folder

class Folder:
    def __init__(self, dir_path:str):
        #a Lumber has a path, which is the folder we want to examine
        self.dir_path = dir_path
        self.subpaths = []
        self.file_path_list = []
        self.file_names = []
        self.size_list = []
        self.folder_paths = []
        self.extensions = []
        self.create_times = []
        self.mod_times = []
        self.acc_times = []
        self.errors = []


    def get_sub_paths(self, dir_path:str):

        ''' Method To Take in a path, add paths to self.subpaths'''
        

        for path, sub_dirs, files in os.walk(dir_path):

            self.subpaths.append(path)

        return 'subdirectories found'

    def investigate_folder(self, subpaths):
     
        '''Take in a list of paths, and return 5 lists with relevant information'''

        #iterate through the path list
        for p in subpaths:

            #iterate through the folder at the path using os.scandir
            for entry in os.scandir(p):

                #confirm that the entry is a file
                if entry.is_file():

                    #output file info
                    print(f'found file {entry.name}')

                    try:
                        #fix slashes in p
                        pst = p.split('/')

                        p = '\\'.join(pst)

                        #get the full file path
                        fullstring = f'{p}\\{entry.name}'                     

                        #this function get the size of a file or folder in bytes
                        file_size = os.path.getsize(entry)

                        #convert file size to mb
                        mb_conv = 1048576

                        size_mb = file_size/mb_conv

                        #get the file extension
                        splits = entry.name.split('.')

                        ext = splits[-1].lower()

                        #get time of creation
                        creat = os.path.getctime(entry)

                        #get time of last modification
                        mod_t = os.path.getmtime(entry)

                        #get access time for each file
                        acc = os.path.getatime(entry)

                        #function to process times
                        def process_time(t_var):

                            #convert to a timestamp
                            timest = time.ctime(t_var)

                            #reformat the timestamp to a string
                            tstr = time.strptime(timest)

                            tfin = time.strftime("%Y_%m_%d", tstr)

                            return tfin
                        
                        #get a processed version of the creation time
                        tcre = process_time(creat)

                        #get a processed version of the modification time
                        tmod = process_time(mod_t)

                        #get a proccessed version of access time
                        tacc = process_time(acc)

                        #append to relevant list
                        self.create_times.append(tcre)

                        self.mod_times.append(tmod)

                        self.acc_times.append(tacc)

                        #take down the folder path
                        self.folder_paths.append(p)

                        #append to the list
                        self.file_path_list.append(fullstring)

                        #append into size list
                        self.size_list.append(size_mb)

                        #append ext to extensions list
                        self.extensions.append(ext)

                        #append the name to the names folder
                        self.file_names.append(entry.name)
                    
                    except:

                        print(f'procedure failed for {p}\\{entry.name}')

                        self.errors.append(f'{p}\\{entry.name}')
        
        if self.errors:

            print(f'the following files were found to have errors: {self.errors}')

        return f'folder at {self.dir_path} fully investigated'

    def investigate_data_out(self, bottom:float) -> object:
        #folder_paths, file_names, file_path_list, extensions, create_times, mod_times, acc_times, size_list
        file_info_df = pd.DataFrame({'sub_folder' : self.folder_paths, 'file_name':self.file_names, 'full_file_path': self.file_path_list, 'extension': self.extensions, 
        'created': self.create_times, 'last_mod': self.mod_times, 'last_accessed': self.acc_times ,'size': self.size_list })

        file_info_df['size'] = file_info_df['size'].astype(float)

        file_info_df = file_info_df[file_info_df['size'] >= float(bottom)]

        return file_info_df

    def move_files(self, file_names:object, file_paths:object, dest_path:str ) -> str:
        ''' Take in a list of file paths and names then use shutil to relocate them to the dest_path'''

        #loop through the file names and file paths together
        for n, p in zip(file_names, file_paths):
            dest = f'{dest_path}/{n}'
            try:
                sht.copy2(p, dest)
                print(f'file {n} moved sucessfully')
        
            except:
                print(f'file {n} could not be moved')

        return 'copy action terminated'

    #optional analysis methods
    #size
    @staticmethod
    def size_anal(df:object, group_key:str)->object:
        fldr_cts = df.groupby(group_key).count()

        fldr_cts = fldr_cts.reset_index()

        fldr_cts = fldr_cts.rename(columns = {'size': 'file_count'})

        fldr_sum = df.groupby(group_key).sum()

        fldr_sum = fldr_sum.reset_index()

        fldr_sum = fldr_sum.rename(columns = {'size': 'total_size_mb'})

        fldr_sz = pd.merge(fldr_cts, fldr_sum, on = 'sub_folder', how = 'inner')

        return fldr_sz