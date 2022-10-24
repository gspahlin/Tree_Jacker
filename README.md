# Tree_Jacker
A folder analysis program with gui in PySimpleGUI

Tree Jacker is a simple program designed to help organize large file archives and eliminate redundant files to help you store files more efficiently and 
protect against data loss. Tree Jacker features a graphical user interface (GUI) for ease of use, and a stand alone .exe port. The stand alone should work on 
most machines, but it has been specifically built and tested in a windows environment. This project was built using Python 3.8.3. The GUI environment was 
built using the tkinter version of PySimpleGui. The .exe port was prepared using cx_Freeze. 

<img src="https://github.com/gspahlin/Tree_Jacker/blob/master/readme_pics/ui.png">

# User Interface Explained

The main function of Tree_Jacker is to analyze the content of a directory tree within your file system. It has the 
capability to inform you about the content and size of subfolders, what kinds of files are taking up the most space, and 
whether duplicate files are present. It also has the capability to unpack a complicated directory structure (including 
hidden folders) into a single folder. 

Target Folder - The target folder is the folder for analysis. Specify the target folder by using the "Browse" button to naviagate to the target folder. The 
"Set 
Target Folder" button needs to be used to designate the target folder for analysis. 

Output Folder - This folder will be the destination for analytical outputs. The basic function of Tree_Jacker is to produce a .csv list of files in a folder 
along with creation, modification and access dates, and the sizes of the files. This file and other files resulting from the optional analyses will be 
written to this folder. Use the "Set Output Folder" button the same as with the target folder.

Floor - Tree_Jacker allows a floor for analysis to be set so that small files and system file can be ignored, as they can introduce confusion into your 
analysis. Some system files can be confusing, and can be dropped using this method. If no value is set the default will be zero, and the program will still 
run. 

Optional Analyses - These wil be run if they are checked at the time that the 'Run' button is clicked. 

  Subfolder Size Analysis - This will output a .csv which lists subfolders in your analysis folders, and the amount of storge space they take up, along with 
  the number of files present in those folders.
  
  Storage Use By File Type - This analysis produces a .csv which breaks each subfolder down by the file exensions present. 
  
  Suspected Duplicates - This analysis will look for files with the same name and size and report them in a .csv file. The file will not be written if no 
  files are found with the same size and name
 
 Optional Unpack Operation- This option will copy all of the files from your analysis folder into a folder of your choice without replicating any of the sub 
 folders. Its intended purpose is to aid in the reorganization of folders which have developed compicated internal folder structures. The 'Apply Analysis 
 Floor to  Unpack Operation' option will allow you to move only files at or above your Floor threshold. If it is not enabled, all files will be moved 
 regardless of  your floor value. 

# Setting up an environment to run Tree_Jacker with Anaconda

Tree_Jacker can be run from the .exe provided in this repository, but because of the libraries needed the package is around a 100 MB download. If you have 
python installed and are comfortable setting up a programming environment, Tree_Jacker can be run from the command line. Here are instructions for setting
up your environment and running it that way. 

Open Anaconda Prompt, and execute the following commands:
<br>
$conda create -n  tjack python==3.8.3<br>
$conda activate tjack<br>
$pip install pysimplegui==4.60.3<br>
$pip install pandas==1.0.5<br>
<br>
After this is done the environment is ready. You can run the script from the command line with<br>
$python tree_jacker_v1.py

When running tree_jacker, make sure that tree_folder.py is present in the folder, as this is a module that is called by the main application. 
