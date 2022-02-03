import tkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os,time
import datetime
import shutil
import datetime as dt








def browse_button():
    # Allow user to select a directory and store it in global var
    # called origin_path
    global origin_path
    filename = filedialog.askdirectory()
    origin_path.set(filename)
    print(filename)

def browse_button2():
    # Allow user to select a directory and store it in global var
    # called receiving_path
    global receiving_path
    filename = filedialog.askdirectory()
    receiving_path.set(filename)
    print(filename)

def submitFunction() :
    for root, dirs,files in os.walk(origin_path):
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            shutil.move(path, dest)
    print('Submit button is clicked.')


root = Tk()
origin_path = StringVar()
receiving_path = StringVar()

#First Browse Button Label
lbl1 = Label(master=root,textvariable=origin_path)
lbl1.grid(row=0, column=1)
#Second Browse Button Label
lbl1_2 = Label(master=root,textvariable=receiving_path)
lbl1_2.grid(row=1, column=1)

lbl1_3 = Label(master=root)
lbl1_3.grid(row=2, column=1)

button = Button(text="Browse", command=browse_button)
button.grid(row=0, column=3)

button2 = Button(text="Browse", command=browse_button2)
button2.grid(row=1, column=3)

scan_btn=Button(text="Scan", command = lambda:submitFunction())
scan_btn.grid(row=2, column=7)

mainloop()

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
created = 'origin_path'
dest = 'receiving_path'
file_path = 'file:///'+os.getcwd()+'/' + ''

print("Last modified: %s" % time.ctime(os.path.getmtime(file_path)))
print("Created: %s" % time.ctime(os.path.getctime(file_path)))

for root, dirs,files in os.walk(origin_path):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.move(path, dest)
            # this is actual move


def find_info(): #this first func. works fine.for root, dirs, files in os.walk(created):
    for root, dirs, files in os,walk(origin_path):
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)                          
    if mtime > ago:
        print(True)
    else:
        print(False)



print (find_info())                           
print (move())                               

print (os.listdir(dest))
print (os.listdir(created))
