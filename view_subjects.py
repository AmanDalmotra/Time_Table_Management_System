from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3

class view:
    def search(self):
        self.t1.delete(*self.t1.get_children())
        s="select * from subjects where subjectcode='"+self.cb1.get()+"' and semester='"+self.cb2.get()+"'"
        self.cr=self.conn.cursor()
        self.cr.execute(s)
        ans=self.cr.fetchall()

        i=0
        for r in ans:
            self.t1.insert('',index=i,values=r)


    def __init__(self):
        self.root=Tk()
        self.conn=sqlite3.connect("timetable.sqlite3")
        self.p1=PanedWindow(self.root)

        self.p2=PanedWindow(self.root)



        self.lb1=Label(self.p1,text="Select Subject Code")
        self.lb2=Label(self.p1,text="Select Semester")
        s="select subjectcode from subjects"
        self.cr=self.conn.cursor()
        self.cr.execute(s)
        ans=self.cr.fetchall()

        x=[]
        for r in ans:
            x.append(r[0])

        self.cb1=Combobox(self.p1,values=r,state="readonly")
        self.cb2=Combobox(self.p1,values=[1,2,3,4,5,6,7,8,9,10,11,12],state="readonly")
        self.bt1=Button(self.p1,text="Search",command=self.search)

        self.t1=Treeview(self.p2,columns=("subjectcode","subjectname","semester","degreename"))
        self.t1.heading("subjectcode",text="Subject Code")
        self.t1.heading("subjectname",text="Subject Name")
        self.t1.heading("semester",text="Semester")
        self.t1.heading("degreename",text="Degree Name")
        self.t1["show"]="headings"

        self.t1.pack()

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=0,column=2)
        self.cb1.grid(row=0,column=1)
        self.cb2.grid(row=0,column=4)
        self.bt1.grid(row=0,column=5)


        self.p1.pack()
        self.p2.pack()

        self.root.mainloop()

