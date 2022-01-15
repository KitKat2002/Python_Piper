import sqlite3
import re

#Utilizes sqlite three to connect to cst database
conn = sqlite3.connect("cst.db")

#connects to the cursor and creates the table tbl_customerinfo and fills it with 3 columns
with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_customerinfo( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_email TEXT \
            )")
    conn.commit()
conn.close()
#__________________________________________________________

#connects to the database and inserts data into the columns
conn = sqlite3.connect("cst.db")

with conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tbl_customerinfo (col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                    ('Shane', 'Hathaway', 'leavemealone@yahoo.com'))

    cursor.execute("INSERT INTO tbl_customerinfo (col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                    ('James', 'Esponage', 'EsJames@protonmail.com'))

    cursor.execute("INSERT INTO tbl_customerinfo (col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                    ('Tiffany', 'Smith', 'Tiff99@gmail.com'))

    cursor.execute("INSERT INTO tbl_customerinfo (col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                    ('Henry', 'Nehlver', 'Nehry@outlook.com'))    
    conn.commit()
conn.close()

#________________________________________________________
#Connects to the database and returrns from the database from the table tbl_customer info an
conn = sqlite3.connect("cst.db")

with conn:
    cursor = conn.cursor()
    cursor.execute("Select col_fname, col_lname, col_email FROM tbl_customerinfo WHERE col_fname = 'Shane'")
    varPerson = cursor.fetchall()
    for item in varPerson:
        msg = "First Name: ()\nLast Name: ()\nEmail: ()".format(item[0],item[1],item[2])
    print(msg)
    conn.commit()
conn.close()

#_______________________________________________________
#Connects to the dataabase and filters the list of files for only ones ending in txt
conn = sqlite3.connect("cst.db")

fileList = ['information.docx', 'Hello.txt', 'myImage.png', \
          'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']

def Filter(datalist):
    return [val for val in datalist
        if re.search(r'.txt', val)]

FilteredList = (Filter(fileList))
print(FilteredList)

#Creates a table and a couple of columns
with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_lists( \
            ID INTEGER PRIMARY KEY, \
            col_1 TEXT, \
            col_2 TEXT \
            )")
    conn.commit()
conn.close()

#____________________________________________________________
conn = sqlite3.connect("cst.db")
#inserts the filtered list into the database
with conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tbl_lists (col_1, col_2) VALUES(?, ?)", \
                   (FilteredList))
