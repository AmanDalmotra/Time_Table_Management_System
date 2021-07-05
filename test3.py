#To edit/delete degree name and description

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

import sqlite3

class editdelete:
    def reset(self):
        self.cb1.set('')
        self.txt1.delete(0,'end')



    def update(self):
        self.conn = sqlite3.connect("timetable.sqlite3")
        self.cr = self.conn.cursor()
        u = "update programs set description= '"+self.txt1.get()+"' where degreename='" + self.cb1.get() + "'"
        self.cr.execute(u)
        self.conn.commit()
        showinfo("", "Updated Successfully")


    def remove(self):
        self.conn = sqlite3.connect("timetable.sqlite3")
        self.cr = self.conn.cursor()
        s = "delete from programs where degreename='" + self.cb1.get() + "'"
        self.cr.execute(s)
        self.conn.commit()
        showinfo("","Deleted Successfully")


    def search(self):
        self.conn=sqlite3.connect("timetable.sqlite3")
        self.cr=self.conn.cursor()
        s="select * from programs where degreename='"+self.cb1.get()+"'" #degreename jo combobox me select kr rhe usko hi get kre bas
        self.cr.execute(s)
        s=self.cr.fetchone() # s variable me ab uski description ko get kr rhe hai
        self.txt1.insert(0,str(s[1]))



    def __init__(self):


        self.root=Tk()
        self.root.geometry("600x200")
        self.root.configure(bg="light blue")
        self.root.configure(padx=5,pady=5)
        p=[]
        self.conn=sqlite3.connect("timetable.sqlite3")
        self.cr=self.conn.cursor()
        s="select * from programs"
        self.cr.execute(s)
        result=self.cr.fetchall()

        for r in result:
            p.append(r[0])

        self.lb3=Label(self.root,text="Time Table Management",background="yellow",relief="solid",anchor="center",font=("arial",9,"bold"))

        self.lb1=Label(self.root,text="PROGRAM NAME",background="white",relief="solid",font=("arial",9,"bold"))

        self.cb1=Combobox(self.root,state="readonly",value=p,width="50")


        self.bt1=Button(self.root,text="SEARCH",command=self.search)


        self.lb2=Label(self.root,text="DESCRIPTION",background="white",relief="solid",font=("arial",9,"bold"))


        self.txt1=Entry(self.root,width="50")


        self.bt2=Button(self.root,text="DELETE",command=self.remove)

        self.bt3=Button(self.root,text="UPDATE",command=self.update)
        self.bt4=Button(self.root,text="RESET",command=self.reset)

        self.lb3.grid(row=0,column=1)
        self.lb1.grid(row=1,column=0)
        self.cb1.grid(row=1,column=1)
        self.bt1.grid(row=1,column=2)
        self.lb2.grid(row=2,column=0)
        self.txt1.grid(row=2,column=1)
        self.bt2.grid(row=2,column=2)
        self.bt3.grid(row=3,column=2)
        self.bt4.grid(row=4,column=2)

        self.root.mainloop()

