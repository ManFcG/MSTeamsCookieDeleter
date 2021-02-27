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
from tkinter import *
from tkinter import messagebox

# TKINTER COMMANDS

win = Tk()
win.title(" COOKIE DELETER ")
win.geometry("500x300") 

T = Text(win, height = 5, width = 52)  

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
info = """There should be a discord button here. If you don't have one, fear not, you just don't have the discord app"""
def teams():
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
  messagebox.showinfo(None, 'Done! your cookies was deleted!')
def discord():
  os.remove(discord_dir1)
  os.remove(discord_dir2)
  messagebox.showinfo(None, 'Done! your cookies was deleted!')

# BUTTONS

button1 = Button(win, text="Clear Teams Cookies", command=teams)
button2 = Button(win, text="Clear Discord Cookies", command=discord)

# IF'S

if path.exists(discord_dir0) == True:
  button2.pack()
else:
  T.insert(END, info) 
  T.pack()

# LOOPS, PACKS, GRIDS
button1.pack()
win.mainloop()
