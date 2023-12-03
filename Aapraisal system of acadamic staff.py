# My college project...
#Frontend Code

from tkinter import *
import tkinter.messagebox
import acadamicdatabase
import tempfile,os

madara=Tk()
madara.title("Appraisal System Of Academic Staff")
#madara.config(bg="#f1c159")
madara.resizable(True,True)
madara.geometry()


Mainframe=Frame(madara,bd=10,width=1520,height=1000,relief=RIDGE)
Mainframe.grid()

Topframe1=Frame(Mainframe,bd=10,width=1510,height=50,relief=RIDGE)
Topframe1.grid(row=2,column=0)

Topframe2=LabelFrame(Mainframe,bd=10,width=1510,height=275,relief=RIDGE,font=("arial",12,"bold"),text="Display:")
Topframe2.grid(row=1,column=0)

Topframe3=Frame(Mainframe,bd=10,width=1510,height=500,relief=RIDGE,bg="#f1c159")
Topframe3.grid(row=0,column=0)

heading=LabelFrame(Topframe3,width=1000,height=40,relief=RIDGE,text="«««««««««««« Appraisal System Of Academic Staff »»»»»»»»»»»»",font=("arial",20,"bold"),bg="#f1c159")
heading.pack(side=TOP)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

leftframe=LabelFrame(Topframe3,bd=5,width=1510,height=500,padx=2,bg="#f1c159",relief=RIDGE,font=("arial",12,"bold"),text="Faculty Profile:")
leftframe.pack(side=LEFT)

leftframe1=Frame(leftframe,bd=5,width=750,height=450,padx=4,pady=2,bg="#f1c159",relief=RIDGE)
leftframe1.pack(side=TOP)

leftframe2=LabelFrame(leftframe,bd=5,width=500,height=350,padx=4,pady=2,bg="#f1c159",relief=RIDGE,font=("arial",12,"bold"),text="Courses:")
leftframe2.pack(side=TOP)

rightframe=LabelFrame(Topframe3,bd=5,width=375,height=500,padx=2,bg="#f1c159",relief=RIDGE,font=("arial",12,"bold"),text="Prints:")
rightframe.pack(side=RIGHT)
rightframe1=Frame(rightframe,bd=5,width=365,height=450,padx=4,pady=4,bg="#f1c159",relief=RIDGE)
rightframe1.pack(side=TOP)

rightframe2=LabelFrame(Topframe3,bd=5,width=345,height=500,padx=2,bg="#f1c159",relief=RIDGE,font=("arial",12,"bold"),text="Research Solar:")
rightframe2.pack(side=RIGHT)
rightframe2a=Frame(rightframe2,bd=5,width=325,height=450,padx=2,bg="#f1c159",relief=RIDGE)
rightframe2a.pack(side=TOP)

#+++++++++++++++++++++++++++++++++++++++++++++++++veriable++++++++++++++++++++++++++++++++++++++++++++++++++++

global As
Name=StringVar()
Designation=StringVar()
Date_Of_Joining=StringVar()
Qualification=StringVar()
Contact=StringVar()
Email_ID=StringVar()
Research_Guide=StringVar()
Date_Of_Registration=StringVar()
Research_Topic=StringVar()
Name_of_Courses=StringVar()
Eligibility=StringVar()
Duration=StringVar()

#++++++++++++++++++++++++++++++++++++++++Fuctions++++++++++++++++++++++++++++++++++++++++++++++++++

def addData():
    if(len(Name.get())!=0):
        acadamicdatabase.addacadamicRec(Name.get(),Designation.get(),Qualification.get(),Date_Of_Joining.get(),Contact.get(),Email_ID.get(),Research_Guide.get(),Date_Of_Registration.get(),Research_Topic.get(),Name_of_Courses.get(),Eligibility.get(),Duration.get())
        lstcourses.delete(0,END)
        lstcourses.insert(END,(Name.get(),Designation.get(),Qualification.get(),Date_Of_Joining.get(),Contact.get(),Email_ID.get(),Research_Guide.get(),Date_Of_Registration.get(),Research_Topic.get(),Name_of_Courses.get(),Eligibility.get(),Duration.get()))

def displaydata():
    lstcourses.delete(0,END)
    for row in acadamicdatabase.viewdata():
        lstcourses.insert(END,row,str(""))

def acadamicRec(event):
    global As
    searchAs=lstcourses.curselection()[0]
    As=lstcourses.get(searchAs)

    entname.delete(0,END)
    entname.insert(END,As(1))
    entdesig.delete(0,END)
    entdesig.insert(END,As(2))
    entqual.delete(0,END)
    entqual.insert(END,As(3))
    entdate.delete(0, END)
    entdate.insert(END, As(4))
    entcont.delete(0, END)
    entcont.insert(END, As(5))
    entemail.delete(0, END)
    entemail.insert(END, As(6))
    entrea.delete(0, END)
    entrea.insert(END, As(7))
    entdate_of_res.delete(0, END)
    entdate_of_res.insert(END, As(8))
    entres_top.delete(0, END)
    entres_top.insert(END, As(9))
    entname_of_course.delete(0, END)
    entname_of_course.insert(END, As(10))
    enteli.delete(0, END)
    enteli.insert(END, As(11))
    entduration.delete(0, END)
    entduration.insert(END, As(12))

def deletedata():
    if (len(Name.get()) != 0):
        acadamicdatabase.deleteRec()
        Reset()
        displaydata()

def searchdata():
    lstcourses.delete(0,END)
    for row in acadamicdatabase.searchdata(Name.get(),Designation.get(),Qualification.get(),Date_Of_Joining.get(),Contact.get(),Email_ID.get(),Research_Guide.get(),Date_Of_Registration.get(),Research_Topic.get(),Name_of_Courses.get(),Eligibility.get(),Duration.get()):
        lstcourses.insert(END,row,str(""))

def updatedata():
    if (len(Name.get()) != 0):
        acadamicdatabase.deleteRec()
    if (len(Name.get()) != 0):
        acadamicdatabase.updatedata(Name.get(),Designation.get(),Qualification.get(),Date_Of_Joining.get(),Contact.get(),Email_ID.get(),Research_Guide.get(),Date_Of_Registration.get(),Research_Topic.get(),Name_of_Courses.get(),Eligibility.get(),Duration.get())
        lstcourses.delete(0, END)
        lstcourses.insert(END,(
        Name.get(), Designation.get(), Qualification.get(), Date_Of_Joining.get(), Contact.get(), Email_ID.get(),
        Research_Guide.get(), Date_Of_Registration.get(), Research_Topic.get(), Name_of_Courses.get(),
        Eligibility.get(), Duration.get()))

def print():
    p=Txtreceipt.get("1.0","end-1c")
    filename= tempfile.mktemp(".txt")
    open(filename,"w").write(p)
    os.startfile(filename,"print")

def Reset():
    Name.set("")
    Designation.set("")
    Date_Of_Joining.set("")
    Qualification.set("")
    Contact.set("")
    Email_ID.set("")
    Research_Guide.set("")
    Date_Of_Registration.set("")
    Research_Topic.set("")
    Name_of_Courses.set("")
    Eligibility.set("")
    Duration.set("")
    Txtreceipt.delete("1.0",END)

def quit():
    quait=tkinter.messagebox.askyesno("Appraisal System Of Academic Staff","Do you want to close the window")
    if quait>0:
        madara.destroy()
        return

#++++++++++++++++++++++++++++++++++++++++++++receipt++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Txtreceipt=Text(rightframe1,height=30,width=42,bd=10,font=("arial",9,"bold"))
Txtreceipt.grid(row=0,column=0)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

lblLabl=Label(Topframe2,bg="#f1c159",font=("arial",10,"bold"),padx=6,pady=2,text="Name          \tDesignation     \t\tQualification    \t\tDate_Of_Joining  \t\tContact  \tEmail_Id \tReserch_guide   \tName_of_the_courses   \tEligibility \tDuration")
lblLabl.grid(row=0,column=0)
#++++++++++++++++++++++++++++++++++++++++listbox and scroll bar+++++++++++++++++++++++++++++++++++++++++++++++

scrollbar=Scrollbar(Topframe2)
scrollbar.grid(row=1,column=1,sticky="ns")

lstcourses=Listbox(Topframe2,width=210,height=5,bg="#f1c159",font=("arial",9,"bold"),yscrollcommand=scrollbar.set)
lstcourses.bind("<<ListboxSelect>>",acadamicRec)
lstcourses.grid(row=1,column=0,padx=1,sticky="nsew")
scrollbar.config(command=lstcourses.xview)

#+++++++++++++++++++++++++++++++++++++Weiget+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

lblname=Label(leftframe1,text="Name:",font=("arial",12,"bold"),bd=7,anchor="w")
lblname.grid(row=0,column=0)
entname=Entry(leftframe1,textvariable=Name,font=("arial",12,"bold"),bd=5,width=50)
entname.grid(row=0,column=1)

lbldesig=Label(leftframe1,text="Designation:",font=("arial",12,"bold"),bd=7,anchor="w")
lbldesig.grid(row=2,column=0)
entdesig=Entry(leftframe1,textvariable=Designation,font=("arial",12,"bold"),bd=5,width=50)
entdesig.grid(row=2,column=1)

lblqual=Label(leftframe1,text="Qualification:",font=("arial",12,"bold"),bd=7,anchor="w")
lblqual.grid(row=4,column=0)
entqual=Entry(leftframe1,textvariable=Qualification,font=("arial",12,"bold"),bd=5,width=50)
entqual.grid(row=4,column=1)

lbldate_of_joining=Label(leftframe1,text="Date_Of_Joining:",font=("arial",9,"bold"),bd=7,anchor="w")
lbldate_of_joining.grid(row=5,column=0)
entdate=Entry(leftframe1,textvariable=Date_Of_Joining,font=("arial",9,"bold"),bd=5)
entdate.grid(row=5,column=1)

lblcont=Label(leftframe1,text="Contact:",font=("arial",12,"bold"),bd=7)
lblcont.grid(row=6,column=0)
entcont=Entry(leftframe1,textvariable=Contact,font=("arial",12,"bold"),bd=5,width=50)
entcont.grid(row=6,column=1)

lblemail=Label(leftframe1,text="Email_Id:",font=("arial",12,"bold"),bd=7,anchor="w")
lblemail.grid(row=8,column=0)
entemail=Entry(leftframe1,textvariable=Email_ID,font=("arial",12,"bold"),bd=5,width=50)
entemail.grid(row=8,column=1)

lblname_of_course=Label(leftframe2,text="Name_Of_Course:",font=("arial",12,"bold"),bd=7,anchor="w")
lblname_of_course.grid(row=0,column=0)
entname_of_course=Entry(leftframe2,textvariable=Name_of_Courses ,font=("arial",12,"bold"),bd=5,width=50)
entname_of_course.grid(row=0,column=1)

lbleli=Label(leftframe2,text="Eligibility:",font=("arial",12,"bold"),bd=7)
lbleli.grid(row=1,column=0)
enteli=Entry(leftframe2,textvariable=Eligibility,font=("arial",12,"bold"),bd=5,width=50)
enteli.grid(row=1,column=1)

lblduration=Label(leftframe2,text="Duration:",font=("arial",12,"bold"),bd=7,anchor="w")
lblduration.grid(row=2,column=0)
entduration=Entry(leftframe2,textvariable=Duration,font=("arial",12,"bold"),bd=5,width=50)
entduration.grid(row=2,column=1)

#+++++++++++++++++++++++++++++++++++++++weigets2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

lblrea=Label(rightframe2a,text="Research Guide:",font=("arial",12,"bold"),bd=7,anchor="w")
lblrea.grid(row=1,column=0)
entrea=Entry(rightframe2a,textvariable=Research_Guide,font=("arial",12,"bold"),bd=5,width=20)
entrea.grid(row=1,column=1)

lbldate_of_res=Label(rightframe2a,text="Date_Of_Registration:",font=("arial",12,"bold"),bd=7,anchor="w")
lbldate_of_res.grid(row=2,column=0)
entdate_of_res=Entry(rightframe2a,textvariable=Date_Of_Registration,font=("arial",12,"bold"),bd=5,width=20)
entdate_of_res.grid(row=2,column=1)

lblres_top=Label(rightframe2a,text="Research_Topic:",font=("arial",12,"bold"),bd=7,anchor="w")
lblres_top.grid(row=3,column=0)
entres_top=Entry(rightframe2a,textvariable=Research_Topic,font=("arial",12,"bold"),bd=4,width=30)
entres_top.grid(row=3,column=1)
#+++++++++++++++++++++++++++++++++++++++++Buttons+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
btnadd=Button(Topframe1,text="Insert",bd=5,bg="#f1c159",font=("arial",12,"bold"),padx=24,width=8,command=addData)
btnadd.grid(row=0,column=0)


btnprint=Button(Topframe1,text="Print",bd=5,bg="#f1c159",font=("arial",12,"bold"),padx=24,width=8,command=print)
btnprint.grid(row=0,column=1)

btndisply=Button(Topframe1,text="Display",bd=5,bg="#f1c159",font=("arial",12,"bold"),padx=24,width=8,command=displaydata)
btndisply.grid(row=0,column=2)

btnupdate=Button(Topframe1,text="Update",bd=5,bg="#f1c159",font=("arial",12,"bold"),padx=24,width=8,command=updatedata)
btnupdate.grid(row=0,column=3)

btndelete=Button(Topframe1,text="Delete",bd=5,bg="#f1c159",font=("arial",12,"bold"),padx=24,width=8,command=deletedata)
btndelete.grid(row=0,column=4)

btnsearch=Button(Topframe1,text="Search",bd=5,bg="#f1c159",font=("arial",12,"bold"),padx=24,width=8,command=searchdata)
btnsearch.grid(row=0,column=5)

btnreset=Button(Topframe1,text="Reset",bd=5,bg="#f1c159",font=("arial",12,"bold"),padx=24,width=8,command=Reset)
btnreset.grid(row=0,column=6)

btnexit=Button(Topframe1,text="Exit",bd=5,bg="#f1c159",font=("arial",12,"bold"),padx=24,width=8,command=quit)
btnexit.grid(row=0,column=7)



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


madara.mainloop()
