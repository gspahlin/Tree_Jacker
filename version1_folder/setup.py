import sys
from cx_Freeze import setup, Executable
#most of the large size is from numpy, try excluding - didn't work
build_exe_options = {'excludes':['numpy']}

base = None

if sys.platform=='win32':
    base='Win32GUI'

#try with base removed (since there is no console with this version)

setup(
    name='Tree Jacker',
    version='1.0',
    description='Application for investigating folder contents',
    #options = {'build_exe':build_exe_options},
    executables = [Executable(script = 'tree_jacker_v1.py', 
    #base=base, 
    icon = 'jack.ico')]
)