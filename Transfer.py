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
    lbl1.delete(0,'end')
    foldername = filedialog.askdirectory()
    lbl1.insert(0,foldername)
    origin_path.set(foldername)

def browse_button2():
    # Allow user to select a directory and store it in global var
    # called receiving_path
    global receiving_path
    lbll_2.delete(0,'end')
    foldername = filedialog.askdirectory()
    lbll_2.insert(0,foldername)
    receiving_path.set(foldername)

def submitFunction() :
    source = lbl1.get()
    files = os.listdir(source)
    for fname in files:
        path = os.path.join(source, fname)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        shutil.move(path, receiving_path.get())
        print('Submit button is clicked.')

root = Tk()
origin_path = StringVar()
receiving_path = StringVar()

#First Browse Button Label
lbl1 = Entry(master=root)
lbl1.grid(row=0, column=1)
#Second Browse Button Label
lbll_2 = Entry(master=root)
lbll_2.grid(row=1, column=1)

button = Button(text="Browse", command=browse_button)
button.grid(row=0, column=3)

button2 = Button(text="Browse", command=browse_button2)
button2.grid(row=1, column=3)

scan_btn=Button(text="Scan", command = lambda:submitFunction())
scan_btn.grid(row=2, column=7)

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
print(ago)
strftime = '%H:%M %m/%d/%Y'
created = 'origin_path'
dest = 'receiving_path'
file_path = os.getcwd()
print(file_path)

print("Last modified: %s" % time.ctime(os.path.getmtime(file_path)))
print("Created: %s" % time.ctime(os.path.getctime(file_path)))

mainloop()

  
for fname in files:
    path = os.path.join(source, fname)
    print(path)
    st = os.stat(path)
    mtime = dt.datetime.fromtimestamp(st.st_mtime)
    if mtime > ago:
        print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
        shutil.move(created, dest)



def find_info(): #this first func. works fine.for root, dirs, files in os.walk(created):
    for fname in files:
        path = os.path.join(source, fname)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)                          
    if mtime > ago:
        print(True)
    else:
        print(False)


##print (find_info())                           
##print (move())                               
