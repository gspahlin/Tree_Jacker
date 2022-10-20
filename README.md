# Tree_Jacker
A folder analysis program with gui in PySimpleGUI

Tree Jacker is a simple program designed to help organize large file archives and eliminate redundant files to help you store files more efficiently and protect
against data loss. Tree Jacker features a graphical user interface (GUI) for ease of use, and a stand alone .exe port. The stand alone should work on most
machines, but it has been specifically built and tested in a windows environment. This project was built using Python 3.8.3. The GUI environment was built using
the tkinter version of PySimpleGui. The .exe port was prepared using cx_Freeze. 

<img src="https://github.com/gspahlin/Tree_Jacker/blob/master/readme_pics/ui.png">

#User Interface Explained

The main function of Tree_Jacker is to analyze the content of a directory tree within your file system. It has the 
capability to inform you about the content and size of subfolders, what kinds of files are taking up the most space, and 
whether duplicate files are present. It also has the capability to unpack a complicated directory structure (including 
hidden folders) into a single folder. 
