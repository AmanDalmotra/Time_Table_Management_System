from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3

class test:

    def reset(self):
        self.cb1.set('')
        self.cb2.set('')
        self.cb3.set('')
        self.cb4.set('')
        self.cb5.set('')
        self.txt.delete(0,'end')

    def exit(self):
        exit()





    def adddata(self):
        s="insert into timetable values(NULL,'"+self.cb3.get()+"','"+self.cb4.get()+"','"+self.cb5.get()+"','"+self.txt1.get()+"')"
        self.cr=self.conn.cursor()
        self.cr.execute(s)
        self.conn.commit()
        showinfo("","Data added successfully")


    #taking function getdata to bind semester and subjectcodes
    def getdata(self,d): #this will take dumy parameter
        s="select subjectcode from subjects"
        #self.cr=self.conn.cursor()
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x=[]
        for r in ans:
            x.append(r[0])
            self.cb3.config(values=x)
    def __init__(self):
        self.root=Tk()

        self.lb1=Label(self.root,text='Select Program')
        self.lb2=Label(self.root,text="Select Semester")
        self.lb3= Label(self.root, text="Select Subject Code ")
        self.lb4= Label(self.root, text="Select Day of Week")
        self.lb5= Label(self.root, text="Select Slot")
        self.lb6= Label(self.root, text="Select Teacher Name")

        self.conn=sqlite3.connect("timetable.sqlite3")
        s="select degreename from programs"
        self.cr=self.conn.cursor()
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x=[]
        for r in ans:
            x.append(r[0])

        self.cb1=Combobox(self.root,values=x,state="readonly")
        self.cb2=Combobox(self.root,values=[1,2,3,4,5,6,7,8,9,10,11,12],state="readonly")
        self.cb2.bind("<<ComboboxSelected>>",self.getdata) #code for binding
        self.cb3=Combobox(self.root,state="readonly")
        self.cb4=Combobox(self.root,values=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],state="readonly")
        self.cb5=Combobox(self.root,state="readonly",values=['9:00am-10:00am','10:00am-11:00am','11:00am-12:00pm','12:00pm-1:00pm','1:00pm-2:00pm','2:00pm-3:00pm','3:00pm-4:00pm','4:00pm-5:00pm'])
        self.txt1=Entry(self.root)

        self.bt1=Button(self.root,text='Add New Data',command=self.adddata)
        self.bt2=Button(self.root,text="Reset",command=self.reset)
        self.bt3=Button(self.root,text="Exit",command=self.exit)

        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)
        self.lb2.grid(row=1,column=0)
        self.cb2.grid(row=1,column=1)
        self.lb3.grid(row=2,column=0)
        self.cb3.grid(row=2,column=1)
        self.lb4.grid(row=3,column=0)
        self.cb4.grid(row=3,column=1)
        self.lb5.grid(row=4,column=0)
        self.cb5.grid(row=4,column=1)
        self.lb6.grid(row=5,column=0)
        self.txt1.grid(row=5,column=1)

        self.bt1.grid(row=6,column=1)
        self.bt2.grid(row=7,column=1)
        self.bt3.grid(row=8,column=1)

        self.root.mainloop()
