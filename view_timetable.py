from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3

class view:
    def reset(self):
        self.cb1.set('')
        self.cb2.set('')
        self.t1.delete(*self.t1.get_children())

    def search(self): #using joint concept
        days=["Monday","Tuesday","Wednesday","Thursday ","Friday ","Saturday"]#list for selecting particular day

        slot8 = ["4:00pm-5:00pm"]  # creating list of all the slots
        for day in days:
            s = "select timetable.teachername, timetable.subjectcode, subjects.subjectname from timetable, subjects where timetable.subjectcode=subjects.subjectcode and timetable.slot='4:00pm-5:00pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester='" + self.cb2.get() + "' and dayofweek='" + day + "'"  # joining subjects and time tables
            self.cr.execute(s)
            ans = self.cr.fetchone()

            if ans != None:
                slot8.append(str(ans[0]) + '-' + str(ans[1]) + '-' + str(ans[2]))
            else:
                slot8.append("Free Lecture")
        self.t1.insert("", index=0, values=slot8)

        slot7 = ["3:00pm-4:00pm"]  # creating list of all the slots
        for day in days:
            s = "select timetable.teachername, timetable.subjectcode, subjects.subjectname from timetable, subjects where timetable.subjectcode=subjects.subjectcode and timetable.slot='3:00pm-4:00pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester='" + self.cb2.get() + "' and dayofweek='" + day + "'"  # joining subjects and time tables
            self.cr.execute(s)
            ans = self.cr.fetchone()

            if ans != None:
                slot7.append(str(ans[0]) + '-' + str(ans[1]) + '-' + str(ans[2]))
            else:
                slot7.append("Free Lecture")
        self.t1.insert("", index=0, values=slot7)

        slot6 = ["2:00pm-3:00pm"]  # creating list of all the slots
        for day in days:
            s = "select timetable.teachername, timetable.subjectcode, subjects.subjectname from timetable, subjects where timetable.subjectcode=subjects.subjectcode and timetable.slot='2:00pm-3:00pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester='" + self.cb2.get() + "' and dayofweek='" + day + "'"  # joining subjects and time tables
            self.cr.execute(s)
            ans = self.cr.fetchone()

            if ans != None:
                slot6.append(str(ans[0]) + '-' + str(ans[1]) + '-' + str(ans[2]))
            else:
                slot6.append("Free Lecture")
        self.t1.insert("", index=0, values=slot6)

        slot5 = ["1:00pm-2:00pm"]  # creating list of all the slots
        for day in days:
            s = "select timetable.teachername, timetable.subjectcode, subjects.subjectname from timetable, subjects where timetable.subjectcode=subjects.subjectcode and timetable.slot='1:00pm-2:00pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester='" + self.cb2.get() + "' and dayofweek='" + day + "'"  # joining subjects and time tables
            self.cr.execute(s)
            ans = self.cr.fetchone()

            if ans != None:
                slot5.append(str(ans[0]) + '-' + str(ans[1]) + '-' + str(ans[2]))
            else:
                slot5.append("Break")
        self.t1.insert("", index=0, values=slot5)

        slot4 = ["12:00pm-1:00pm"]  # creating list of all the slots
        for day in days:
            s = "select timetable.teachername, timetable.subjectcode, subjects.subjectname from timetable, subjects where timetable.subjectcode=subjects.subjectcode and timetable.slot='12:00am-1:00pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester='" + self.cb2.get() + "' and dayofweek='" + day + "'"  # joining subjects and time tables
            self.cr.execute(s)
            ans = self.cr.fetchone()

            if ans != None:
                slot4.append(str(ans[0]) + '-' + str(ans[1]) + '-' + str(ans[2]))
            else:
                slot4.append("Free Lecture")
        self.t1.insert("", index=0, values=slot4)

        slot3 = ["11:00am-12:00pm"]  # creating list of all the slots
        for day in days:
            s = "select timetable.teachername, timetable.subjectcode, subjects.subjectname from timetable, subjects where timetable.subjectcode=subjects.subjectcode and timetable.slot='11:00am-12:00pm' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester='" + self.cb2.get() + "' and dayofweek='" + day + "'"  # joining subjects and time tables
            self.cr.execute(s)
            ans = self.cr.fetchone()

            if ans != None:
                slot3.append(str(ans[0]) + '-' + str(ans[1]) + '-' + str(ans[2]))
            else:
                slot3.append("Free Lecture")
        self.t1.insert("", index=0, values=slot3)

        slot2 = ["10:00am-11:00am"]  # creating list of all the slots
        for day in days:
            s = "select timetable.teachername, timetable.subjectcode, subjects.subjectname from timetable, subjects where timetable.subjectcode=subjects.subjectcode and timetable.slot='10:00am-11:00am' and subjects.degreename='" + self.cb1.get() + "' and subjects.semester='" + self.cb2.get() + "' and dayofweek='" + day + "'"  # joining subjects and time tables
            self.cr.execute(s)
            ans = self.cr.fetchone()

            if ans != None:
                slot2.append(str(ans[0]) + '-' + str(ans[1]) + '-' + str(ans[2]))
            else:
                slot2.append("Free Lecture")
        self.t1.insert("", index=0, values=slot2)

        slot1=["9:00am-10:00am"]  #creating list of all the slots
        for day in days:
            s="select timetable.teachername, timetable.subjectcode, subjects.subjectname from timetable, subjects where timetable.subjectcode=subjects.subjectcode and timetable.slot='9:00am-10:00am' and subjects.degreename='"+self.cb1.get()+"' and subjects.semester='"+self.cb2.get()+"' and dayofweek='"+day+"'" #joining subjects and time tables
            self.cr.execute(s)
            ans= self.cr.fetchone()

            if ans!=None:
                slot1.append(str(ans[0])+'-'+str(ans[1])+'-'+str(ans[2]))
            else:
                slot1.append("Free Lecture")
        self.t1.insert("",index=0,values=slot1)


    def __init__(self):
        self.root=Tk()
        self.conn=sqlite3.connect("timetable.sqlite3")
        self.p1=PanedWindow(self.root)

        self.p2=PanedWindow(self.root)



        self.lb1=Label(self.p1,text="Select Degree Name")
        self.lb2=Label(self.p1,text="Select Semester")
        s="select degreename from programs"
        self.cr=self.conn.cursor()
        self.cr.execute(s)
        ans=self.cr.fetchall()

        x=[]
        for r in ans:
            x.append(r[0])

        self.cb1=Combobox(self.p1,values=x,state="readonly")
        self.cb2=Combobox(self.p1,values=[1,2,3,4,5,6,7,8,9,10,11,12],state="readonly")
        self.bt1=Button(self.p1,text="Search",command=self.search)
        self.bt2=Button(self.p1,text="Reset",command=self.reset)
        self.t1=Treeview(self.p2,columns=("Slot","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"))
        self.t1.heading("Slot",text="Slot")
        self.t1.heading("Monday",text="Monday")
        self.t1.heading("Tuesday",text="Tuesday")
        self.t1.heading("Wednesday",text="Wednesday")
        self.t1.heading("Thursday",text="Thursday")
        self.t1.heading("Friday",text="Friday")
        self.t1.heading("Saturday",text="Saturday")




        self.t1["show"]="headings"

        self.t1.pack()

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=0,column=2)
        self.cb1.grid(row=0,column=1)
        self.cb2.grid(row=0,column=4)
        self.bt1.grid(row=0,column=5)
        self.bt2.grid(row=0,column=6)


        self.p1.pack()
        self.p2.pack()

        self.root.mainloop()

