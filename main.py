# LIBRARIES

import os
import sys
import shutil
from os import path

# DIRECTORIES

dir1 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Cookies')
dir2 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Cookies-journal')
dir3 = path.expandvars(r'%APPDATA%\Microsoft\Teams\tmp')
dir4 = path.expandvars(r'%APPDATA%\Microsoft\Teams\blob_storage')
dir5 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Cache')
dir6 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Session Storage')
dir7 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Local Storage')

# REMOVE COMMANDS

os.remove(dir1)
os.remove(dir2)
shutil.rmtree(dir4)
shutil.rmtree(dir5)
shutil.rmtree(dir6)
shutil.rmtree(dir7)

if os.path.isdir(dir3) == True:
    shutil.rmtree(dir3)
else:
    print("Folder TEMP/tmp doesn't exists!")