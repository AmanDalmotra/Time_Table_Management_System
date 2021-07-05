from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3




class add:
    def reset(self):
        self.txt1.delete(0,'end')
        self.txt2.delete(0,'end')
        self.cb1.set('')
        self.txt4.set('')




    def insert(self):

        s = "insert into subjects values('" + self.txt1.get() + "','" + self.txt2.get() + "','"+self.cb1.get()+"','"+self.txt4.get()+"')"

        self.cr.execute(s)
        self.conn.commit()
        self.conn.close()
        showinfo('',"subjects added successfully")

    def __init__(self):
        self.root=Tk()
        self.conn = sqlite3.connect("timetable.sqlite3")



        self.lb1=  Label(self.root,text="Enter subject Code")
        self.lb2 = Label(self.root, text="Enter Subject Name")
        self.lb3 = Label(self.root, text="Enter Semester")
        self.lb4 = Label(self.root, text="Enter Degree Name")

        self.txt1=Entry(self.root)
        self.txt2=Entry(self.root)
        self.cb1=Combobox(self.root,values=[1,2,3,4,5,6,7,8,9,10,11,12],state="readonly")

        s="select degreename from programs"
        self.cr = self.conn.cursor()
        self.cr.execute(s)
        ans=self.cr.fetchall() #fetching all values from programs table

        x=[] #creating empty list
        for r in ans:
            x.append(r[0]) #appending only degreename not description


        self.txt4=Combobox(self.root, values=x,state="readonly") # now since anyone can write the wrong spelling of subjects so its better to fetch subjects from programs

        self.bt1=Button(self.root,text="Submit",command=self.insert)
        self.bt2=Button(self.root,text="Reset",command=self.reset)
        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1, column=0)
        self.lb3.grid(row=2, column=0)
        self.lb4.grid(row=3, column=0)

        self.txt1.grid(row=0,column=1)
        self.txt2.grid(row=1, column=1)
        self.cb1.grid(row=2, column=1)
        self.txt4.grid(row=3, column=1)

        self.bt1.grid(row=4,column=1)
        self.bt2.grid(row=5,column=1)

        self.root.mainloop()

