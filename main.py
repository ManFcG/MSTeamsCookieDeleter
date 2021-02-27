# CREATED BY
#___  ___           ______   _____
#|  \/  |           |  ___| |  __ \
#| .  . | __ _ _ __ | |_ ___| |  \/
#| |\/| |/ _` | '_ \|  _/ __| | __ 
#| |  | | (_| | | | | || (__| |_\ \
#\_|  |_/\__,_|_| |_\_| \___|\____/

# LIBRARIES
import os
import sys
import shutil
from os import path

# DIRECTORIES

teams_dir1 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Cookies')
teams_dir2 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Cookies-journal')
teams_dir3 = path.expandvars(r'%APPDATA%\Microsoft\Teams\tmp')
teams_dir4 = path.expandvars(r'%APPDATA%\Microsoft\Teams\blob_storage')
teams_dir5 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Cache')
teams_dir6 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Session Storage')
teams_dir7 = path.expandvars(r'%APPDATA%\Microsoft\Teams\Local Storage')

discord_dir0 = path.expandvars(r'%APPDATA%\discord')
discord_dir1 = path.expandvars(r'%APPDATA%\discord\Cookies')
discord_dir2 = path.expandvars(r'%APPDATA%\discord\Cookies-journal')

# REMOVE COMMANDS
if path.exists(discord_dir0) == True:
    print("Hi!")
    print("What cookies you want to delete?")
    print(" ")
    print("1. Teams")
    print("2. Discord")
    print(" ")
    a = int(input("Your choose: "))
    if a == 1:
        os.remove(teams_dir1)
        os.remove(teams_dir2)
        shutil.rmtree(teams_dir4)
        shutil.rmtree(teams_dir5)
        shutil.rmtree(teams_dir6)
        shutil.rmtree(teams_dir7)
        if os.path.isdir(teams_dir3) == True:
            shutil.rmtree(teams_dir3)
        else:
            print("Folder TEMP/tmp doesn't exists!")
            print("Done! your cookies was deleted!")
    if a == 2:
        os.remove(discord_dir1)
        os.remove(discord_dir2)
        print("Done! your cookies was deleted!")
else:
    os.remove(teams_dir1)
    os.remove(teams_dir2)
    shutil.rmtree(teams_dir4)
    shutil.rmtree(teams_dir5)
    shutil.rmtree(teams_dir6)
    shutil.rmtree(teams_dir7)
    if os.path.isdir(teams_dir3) == True:
        shutil.rmtree(teams_dir3)
    else:
        print("Folder TEMP/tmp doesn't exists!")
        print("Done! your cookies was deleted!")
