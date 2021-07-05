#To add degreename and description
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

import sqlite3


class demo:
    def exit(self):
        exit()
    def demo(self):
        conn = sqlite3.connect("timetable.sqlite3")
        ps="select * from programs"
        cr = conn.cursor() # cr is variable to make it act as cursor
        cr.execute(ps)
        ans=cr.fetchall()
        flag= False
        for r in ans:
            if str(r[0]).upper()==self.txt1.get().upper():
                flag= True
                break
        if flag==True:
            showinfo("invalid","Duplicate course name")
        if self.txt1.get()=="" or self.txt2.get()=="":
            showinfo("invalid","please fill the requirements")

        else:

            # s= "insert into programs values('B.tech- CSE','4 year engineering graduation')" #creating query in python file
            #degree = input("enter program name")
            #desc = input("enter description")

            s = "insert into programs values('" + self.txt1.get() + "','" + self.txt2.get() + "')"

            cr.execute(s)
            conn.commit()
            showinfo("","data insertion successfull")
            print("row inserted successfull")



    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x100")
        self.root.configure(bg="light blue")

        self.lb1=Label(self.root, text="ENTER DEGREE", relief="solid", font=("arial",9,"bold"))
        self.txt1=Entry(self.root)
        self.lb2=Label(self.root,text="ENTER DESCRIPTION", relief="solid",font=("arial",9,"bold"))
        self.txt2=Entry(self.root)
        self.bt1=Button(self.root,text="SUBMIT", command=self.demo)
        self.bt2=Button(self.root,text="EXIT",command=self.exit)

        self.lb1.grid(row=0,column=0)
        self.txt1.grid(row=0,column=1)
        self.lb2.grid(row=1,column=0)
        self.txt2.grid(row=1,column=1)
        self.bt1.grid(row=2,column=1)
        self.bt2.grid(row=3,column=1)

        self.root.mainloop()


