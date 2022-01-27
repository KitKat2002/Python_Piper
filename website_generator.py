#iimports the webbrowser operating system and tkinter
import webbrowser
import os
from tkinter import *

#Creates a function holding the webpage format
def Submit(txtfld):
    text = txtfld.get()
    html_template = """
    <html>
    <body>
    <h1>
    {}
    </h1>
    </body>
    </html>
    """.format(text)
    f = open("BasicWebsite.html", "w")
    f.write(html_template)
    f.close()
    webbrowser.open_new_tab("BasicWebsite.html")

filename = 'file:///'+os.getcwd()+'/' + 'BasicWebsite.html'

#Creates the gui for changing the webpage body
window=Tk()
btn=Button(window, text="To change body click here", fg='brown', command = lambda:Submit(txtfld))
btn.place(x=80, y=100)
txtfld=Entry(window, text="", bd=5)
txtfld.place(x=80, y=150)
window.title('Webpage Generator')
window.geometry("300x200+10+10")
window.mainloop()

