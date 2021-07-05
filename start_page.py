

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

import test
import test2
import test3

import add_subjects
import view_subjects

import add_timetable
import view_timetable

class startpage:

    def fire1(self):
        obj=test.demo()

    def fire2(self):
        obj=test2.demo()

    def fire3(self):
        obj=test3.editdelete()

    def fire4(self):
        obj=add_subjects.add()

    def fire5(self):
        obj=view_subjects.view()

    def fire6(self):
        obj=add_timetable.test()

    def fire7(self):
        obj=view_timetable.view()


    def __init__(self):
        self.root=Tk()
        self.root.geometry("1000x800")
        self.root.configure(background="light blue")

        self.lb1=Label(self.root,text="TIME",relief="solid")
        self.lb2=Label(self.root,text="TABLE",relief="solid")
        self.lb3=Label(self.root,text="MANAGEMENT",relief="solid")



        self.mymenu = Menu(self.root) #creating a menubar with name mymenu
        self.root.title("Menu Window")
        self.root.config(menu=self.mymenu)#sticking menu bar on the tk window

        submenu1 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Course", menu=submenu1)
        submenu1.add_command(label="Add New Course",command=self.fire1 )
        submenu1.add_command(label="View All Course",command=self.fire2)
        submenu1.add_command(label="Edit/Delete Courses",command=self.fire3)

        submenu2 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Subjects", menu=submenu2)
        submenu2.add_command(label="Add New Subjects",command=self.fire4)
        submenu2.add_command(label="View Subject Course Wise",command=self.fire5)
        #submenu2.add_command(label="Edit/Delete Subjects")

        submenu3 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Time Table", menu=submenu3)
        submenu3.add_command(label="Add New Time Table",command=self.fire6)
        submenu3.add_command(label="View Time Table",command=self.fire7)
        #submenu3.add_command(label="Edit/Delete Time Table")

        self.lb1.pack()
        self.lb2.pack()
        self.lb3.pack()

        self.root.mainloop()
#-------------------------------------------------
startpage()
