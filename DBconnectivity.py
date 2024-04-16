import sqlite3 as sql
from tkinter import *
from tkinter import messagebox

def setup():
    global cur
    global db
    global connection1
    val1 = str(w3.get())
    val2 = str(w4.get())
    cur.execute("insert into login(usename,password) values(?,?)",(val1,val2))
    messagebox.showinfo("Done!")
    connection1.commit()
    connection1.close()

def login():
    global cur
    global db
    global connection1
    val1 = str(w1.get())
    val2 = str(w2.get())
    cur.execute("SELECT * FROM login WHERE usename=? AND password=?", (val1, val2))
    result = cur.fetchone()

    if result:
        messagebox.showinfo("Permission Granted", "Login Successful. Permission granted!")

    else:
        messagebox.showerror("Permission Denied", "Invalid login credentials. Permission denied.")
    connection1.commit()
    connection1.close()

def signup():
    new_window = Toplevel()
    new_window.title("NewSETUP")
    new_window.geometry("250x250")
    l1 = Label(new_window,text="LoginID: ")
    l1.place(x=20,y=20)

    l2 = Label(new_window,text="Password: ")
    l2.place(x=20,y=50)

    wid3 = Entry(new_window,textvariable = w3)
    wid3.place(x = 70,y= 20)

    wid4 = Entry(new_window,textvariable = w4,show="*")
    wid4.place(x = 80,y= 50)

    b1 = Button(new_window,text = "Submit",command = setup)
    b1.place(x = 20,y = 80)

db = "login.db"
connection1 = sql.connect(db)
cur = connection1.cursor()

root = Tk()
root.title("Welcome!")
root.geometry("250x250")

#cur.execute("CREATE TABLE login(usename text,password text)")

global w1
w1 = StringVar()

global w2
w2 = StringVar()

global w3
w3 = StringVar()

global w4
w4 = StringVar()

l1 = Label(root,text="LoginID: ")
l1.place(x=20,y=20)

l2 = Label(root,text="Password: ")
l2.place(x=20,y=50)

wid1 = Entry(root,textvariable=w1)
wid1.place(x = 70,y= 20)

wid2 = Entry(root,textvariable=w2,show="*")
wid2.place(x = 80,y= 50)

b1 = Button(root,text = "Submit",command = login)
b1.place(x = 20,y = 80)

b2 = Button(root,text = "Sign UP",command = signup)
b2.place(x = 120,y = 80)

root.mainloop()