#To search degree name
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

import sqlite3

class demo:
    def grab(self):
        self.t1.delete(*self.t1.get_children())


        t = "select * from programs"  # creating a query
        self.cr = self.conn.cursor()  # create a cursor in table
        self.cr.execute(t)  # execute query & store in internal object

        ans = self.cr.fetchall()  # get data from internal object and store in ans
        # ans contains a list of tuples
        i=0
        for r in ans:
            if r[0] in self.cb1.get():

                p=(r[0], r[1])
                #print(p)
                self.t1.insert("",index=i,values=p)
                i=i+1# print each element

    def __init__(self):

        self.root=Tk()
        self.root.geometry("500x500")

        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)
        self.root.configure(bg="light blue")


        self.lb1=Label(self.p1,text="Enter Degree Name",relief="solid",font=("arial",9,"bold"))
        self.conn=sqlite3.connect("timetable.sqlite3")
        s="select degreename from programs"
        self.cr=self.conn.cursor()
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x=[]
        for r in ans:
            x.append(r[0])

        self.cb1=Combobox(self.p1,values=x,state="readonly")
        self.lb1.grid(row=0,column=1)
        self.cb1.grid(row=0,column=2)
        self.bt1=Button(self.p1,text="SEARCH",command=self.grab)
        self.bt1.grid(row=0,column=3)

        self.t1=Treeview(self.p2,columns=("degree","description"))

        self.t1.heading("degree",text="Degree Name")
        self.t1.heading("description",text="Description")
        self.t1["show"]="headings"
        self.t1.pack()
        self.p1.pack()
        self.p2.pack()
        self.conn=sqlite3.connect("timetable.sqlite3")
        s = "select * from programs"  # creating a query
        self.cr = self.conn.cursor()  # create a cursor in table
        self.cr.execute(s)  # execute query & store in internal object

        ans = self.cr.fetchall()  # get data from internal object and store in ans
        # ans contains a list of tuples
        i = 0
        for r in ans:
            # read each tuple from list ans
            p = ( r[0], r[1])
            self.t1.insert("",index=i, values=p)
            i += 1  # print each element


        self.root.mainloop()

