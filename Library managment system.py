#Here new project Library Managment System
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tempfile,os

class Library:
    def __init__(self,madara):
        self.madara=madara
        self.madara.title("Library Managment System")
        self.madara.geometry()
        self.madara.config(bg="#f1c159")

        Mtype=StringVar()
        RefrenceNo=StringVar()
        Title=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Mobileno=StringVar()
        BookID=StringVar()
        BookTitle=StringVar()
        Author=StringVar()
        DateBorrowed=StringVar()
        Datedue=StringVar()
        Daysonload=StringVar()
        Datereturnfile=StringVar()
        Sellingprice=StringVar()




        def reset():
            Mtype.set(" ")
            RefrenceNo.set(" ")
            Title.set(" ")
            Firstname.set(" ")
            Surname.set(" ")
            Address.set(" ")
            Postcode.set(" ")
            Mobileno.set(" ")
            BookID.set(" ")
            BookTitle.set(" ")
            Author.set(" ")
            DateBorrowed.set(" ")
            Datedue.set(" ")
            Daysonload.set(" ")
            Datereturnfile.set(" ")
            Sellingprice.set(" ")
            self.printtxt.delete("1.0",END)

        def reciept():
            self.bottomtxt.insert(END,Mtype.get()+"\t\t\t"+RefrenceNo.get()+"\t\t\t"+Title.get()+"\t\t"+Firstname.get()+"\t\t\t"+Surname.get()+"\t\t"+Address.get()+
                                  "\t\t\t"+Postcode.get()+"\t\t\t"+Mobileno.get()+"\t\t\t"+BookTitle.get()+"\t\t\t"+DateBorrowed.get()+"\n")

        def display():
            self.printtxt.insert(END, "Anime_Id:\t\t" + BookID.get() + "\n")
            self.printtxt.insert(END, "Anime_Title:\t\t" + BookTitle.get() + "\n")
            self.printtxt.insert(END,"Member_Type:\t\t"+Mtype.get()+"\n")
            self.printtxt.insert(END,"Refrence_No:\t\t"+RefrenceNo.get()+"\n")
            self.printtxt.insert(END, "Title:\t\t" + Title.get()+"\n")
            self.printtxt.insert(END, "First_name:\t\t" + Firstname.get() + "\n")
            self.printtxt.insert(END, "Sur_name:\t\t" + Surname.get() + "\n")
            self.printtxt.insert(END, "Address1:\t\t" + Address.get() + "\n")
            self.printtxt.insert(END, "Mobile_no:\t\t" + Mobileno.get() + "\n")
            self.printtxt.insert(END, "Date_Borrowed:\t\t" + DateBorrowed.get() + "\n")
            self.printtxt.insert(END, "Author_Name:\t\t" + Author.get() + "\n")
            self.printtxt.insert(END, "Late_return_file:\t\t" + Datereturnfile.get() + "\n")
            self.printtxt.insert(END, "Date_Due:\t\t" + Datedue.get() + "\n")

        def print():
            p=self.printtxt.get("1.0","end-1c")
            filename= tempfile.mktemp(".txt")
            open(filename,"w").write(p)
            os.startfile(filename,"print")

        def Delete():
            reset()
            self.bottomtxt.delete("1.0",END)

        def exit():
            exit = tkinter.messagebox.askyesno("Library Management System", "Do You Want T0 Close The Window")
            if exit>0:
                madara.destroy()
            return


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        Mainframe = Frame(self.madara, bd=8, width=1520, height=1400, relief=RIDGE,bg="#f1c159")
        Mainframe.grid()

        Topframe3 = Frame(Mainframe, bd=8, width=1510, height=100, relief=RIDGE,bg="#f1c159")
        Topframe3.grid(row=2, column=0)

        Topframe2 = LabelFrame(Mainframe, bd=8, width=1510, height=575, relief=RIDGE, font=("arial", 12, "bold"))
        Topframe2.grid(row=1, column=0)

        Topframe1 = Frame(Mainframe, bd=8, width=1510, height=600, relief=RIDGE, bg="#f1c159")
        Topframe1.grid(row=0, column=0)

        heading = LabelFrame(Topframe1, width=1000, height=40, relief=RIDGE,text="«««««««««««« Anime Managment System »»»»»»»»»»»»",font=("arial", 20, "bold"), bg="#f1c159")
        heading.pack(side=TOP)

        leftframe=LabelFrame(Topframe2,text="Library Membership Info:",height=574,width=765,relief=RIDGE,bg="#f1c159",font=("arial", 12, "bold"),bd=5)
        leftframe.grid(row=0,column=0)

        rightframe=LabelFrame(Topframe2,text="Book Details:",bd=5,height=570,width=745,relief=RIDGE,bg="#f1c159",font=("arial",12,"bold"))
        rightframe.grid(row=0,column=1)

        bottomframe=Frame(Mainframe,bd=8, width=1510, height=70, relief=RIDGE,bg="#f1c159")
        bottomframe.grid()
#++++++++++++++++++++++++++++++++++++++Wigets1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        left = Frame(leftframe, relief=RIDGE, bg="#f1c159", bd=5)
        left.grid(row=0, column=0)



        Mtype=ttk.Combobox(left,textvariable=Mtype,font=("arial",10,"bold"),state="readonly",width=20)
        mtype = Label(left, text="Member_Type:", bd=3, font=("arial", 12, "bold"))
        mtype.grid(row=0, column=0, pady=4, padx=10)
        Mtype["value"]=("","Student","Lecturer","Admin_Staff")
        Mtype.grid(row=0,column=1,pady=9,padx=10)
        Mtype.current(0)

        Refrenceno = Label(left, text="RefrenceNo:", bd=3, font=("arial", 12, "bold"))
        Refrenceno.grid(row=1, column=0, pady=4, padx=10)
        RefrenceNoent = Entry(left, font=("aral", 12, "bold"),textvariable=RefrenceNo, bd=3)
        RefrenceNoent.grid(row=1, column=1, pady=9, padx=10)

        Titlee = Label(left, text="Title:", bd=3, font=("arial", 12, "bold"))
        Titlee.grid(row=2, column=0, pady=4, padx=10)
        Titlent=ttk.Combobox(left, font=("aral", 10, "bold"),width=20,textvariable=Title,state="readonly")
        Titlent.grid(row=2, column=1, pady=9, padx=10)
        Titlent["value"]=("","Mr.","Miss.","Ms.","Dr.","Mrs.")
        Titlent.current(0)

        firstname = Label(left, text="Firstname:", bd=3, font=("arial", 12, "bold"))
        firstname.grid(row=3, column=0, pady=4, padx=10)
        firstnameent = Entry(left, font=("aral", 12, "bold"),textvariable=Firstname, bd=3)
        firstnameent.grid(row=3, column=1, pady=9, padx=10)

        surname = Label(left, text="Surname:", bd=3, font=("arial", 12, "bold"))
        surname.grid(row=4, column=0, pady=4, padx=10)
        surnameent = Entry(left, font=("aral", 12, "bold"),textvariable=Surname, bd=3)
        surnameent.grid(row=4, column=1, pady=9, padx=10)

        address= Label(left, text="Address:", bd=3, font=("arial", 12, "bold"))
        address.grid(row=5, column=0, pady=4, padx=10)
        addressent = Entry(left, font=("aral", 12, "bold"), bd=3,textvariable=Address)
        addressent.grid(row=5, column=1, pady=9, padx=10)

        postcode= Label(left, text="Post_Code:", bd=3, font=("arial", 12, "bold"))
        postcode.grid(row=6, column=0, pady=4, padx=10)
        postcodent = Entry(left, font=("aral", 12, "bold"), bd=3,textvariable=Postcode)
        postcodent.grid(row=6, column=1, pady=9, padx=10)

        mobile = Label(left, text="Mobile_No.:", bd=3, font=("arial", 12, "bold"))
        mobile.grid(row=7, column=0, pady=4, padx=10)
        mobilent = Entry(left, font=("aral", 12, "bold"), bd=3,textvariable=Mobileno)
        mobilent.grid(row=7, column=1, pady=12, padx=10)



#+++++++++++++++++++++++++++++++++++++++++++++++Wigets2+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        left1=Frame(leftframe,relief=RIDGE,bg="#f1c159",bd=5)
        left1.grid(row=0,column=1)

        AnimetD = Label(left1, text="AnimeID:", bd=3, font=("arial", 12, "bold"))
        AnimetD.grid(row=0, column=0, pady=4, padx=10)
        Animeent = Entry(left1, font=("aral", 10, "bold"), bd=3,textvariable=BookID)
        Animeent.grid(row=0, column=1, pady=9, padx=10)

        Animetitle= Label(left1, text="AnimeTitle:", bd=3, font=("arial", 12, "bold"))
        Animetitle.grid(row=1, column=0, pady=4, padx=10)
        AnimeTitlent = Entry(left1, font=("aral", 10, "bold"), bd=3,textvariable=BookTitle)
        AnimeTitlent.grid(row=1, column=1, pady=9, padx=10)

        author = Label(left1, text="Author:", bd=3, font=("arial", 12, "bold"))
        author.grid(row=2, column=0, pady=4, padx=10)
        Authorent = Entry(left1, font=("aral", 10, "bold"), bd=3,textvariable=Author)
        Authorent.grid(row=2, column=1, pady=9, padx=10)

        Datebor = Label(left1, text="DateBorrowed:", bd=3, font=("arial", 12, "bold"))
        Datebor.grid(row=3, column=0, pady=4, padx=10)
        Dateborent = Entry(left1, font=("aral", 10, "bold"), bd=3,textvariable=DateBorrowed)
        Dateborent.grid(row=3, column=1, pady=9, padx=10)

        datedue = Label(left1, text="DateDue:", bd=3, font=("arial", 12, "bold"))
        datedue.grid(row=4, column=0, pady=4, padx=10)
        Datedueent = Entry(left1, font=("aral", 10, "bold"), bd=3,textvariable=Datedue)
        Datedueent.grid(row=4, column=1, pady=9, padx=10)

        Daysloan = Label(left1, text="Days_On_Loan:", bd=3, font=("arial", 12, "bold"))
        Daysloan.grid(row=5, column=0, pady=4, padx=10)
        Daysloanent = Entry(left1, font=("aral", 10, "bold"), bd=3,textvariable=Daysonload)
        Daysloanent.grid(row=5, column=1, pady=9, padx=10)

        latereturnfile= Label(left1, text="Late_Return_Fee:", bd=3, font=("arial", 12, "bold"))
        latereturnfile.grid(row=6, column=0, pady=4, padx=10)
        latereturnfileent = Entry(left1, font=("aral", 10, "bold"), bd=3,textvariable=Datereturnfile)
        latereturnfileent.grid(row=6, column=1, pady=9, padx=10)

        selling = Label(left1, text="Selling_Price:", bd=3, font=("arial", 12, "bold"))
        selling.grid(row=7, column=0, pady=4, padx=10)
        sellingent = Entry(left1, font=("aral", 10, "bold"), bd=3,textvariable=Sellingprice)
        sellingent.grid(row=7, column=1, pady=9, padx=10)

        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        printlbl = LabelFrame(rightframe, text="Print", bd=5, height=45, width=345, relief=RIDGE, bg="#f1c159",
                              font=("arial", 12, "bold"))
        printlbl.grid(row=0, column=1)
        self.printtxt = Text(printlbl, bd=5, height=30, width=34, relief=RIDGE)
        self.printtxt.grid(row=0, column=0)

        listlbl = LabelFrame(rightframe, bd=5, height=45, width=345, relief=RIDGE, bg="#f1c159",
                              font=("arial", 12, "bold"))
        listlbl.grid(row=0,column=0)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        scrollbar=Scrollbar(listlbl)
        scrollbar.grid(row=0,column=1,sticky="ns")

        listofanimes = ["Attack_On_Titan", "Demon_Slayer", "Naruto", "God_Of_High_School", "Death_Note",
                        "Dragen_Ball_Z", "Bleach", "One_Punch_Man", "Jujutsu_Kaisen", "Castlevania"]

        def selectbook(evt):
            valuee=str(listbook.get(listbook.curselection()))

            w=valuee

            if (w=="Attack_On_Titan"):
                BookID.set("SBI 85446745")
                BookTitle.set("Attack_On_Titan")
                Author.set("Hajime Isayama")
                Datereturnfile.set("50 rupees")
                Sellingprice.set("900")
                display()

                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=(d1+d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "Demon_Slayer"):
                BookID.set("SBI 239673744")
                BookTitle.set("Demon_Slayer")
                Author.set("Koyoharu Gotouge")
                Datereturnfile.set("50 rupees")
                Sellingprice.set("754")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "Naruto"):
                BookID.set("SBI 297675643")
                BookTitle.set("Demon_Slayer")
                Author.set("Masasshi Kishimoto")
                Datereturnfile.set("50 rupees")
                Sellingprice.set("999")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "God_Of_High_School"):
                BookID.set("SBI 233408785")
                BookTitle.set("God_Of_High_School")
                Author.set("Yongje Park")
                Datereturnfile.set("50 rupees")
                Sellingprice.set("998")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "Death_Note"):
                BookID.set("SBI 34526741")
                BookTitle.set("Death_Note")
                Author.set("Tsugumi Ohba")
                Datereturnfile.set("50 rupees")
                Sellingprice.set("899")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(11)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "Dragen_Ball_Z"):
                BookID.set("SBI 23536741")
                BookTitle.set("Dragen_Ball_Z")
                Author.set("Takao Koyama")
                Datereturnfile.set("50 rupees")
                Sellingprice.set("1299")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "Bleach"):
                BookID.set("SBI 93456740")
                BookTitle.set("Bleach")
                Author.set("Tile Kubo")
                Datereturnfile.set("50 rupees")
                Sellingprice.set("1244")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "One_Punch_Man"):
                BookID.set("SBI 20142344")
                BookTitle.set("One_Punch_Man")
                Author.set("One")
                Datereturnfile.set("90 rupees")
                Sellingprice.set("9090")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "Jujutsu_Kaisen"):
                BookID.set("SBI 847467347")
                BookTitle.set("One_Punch_Man")
                Author.set("Gege Akutami")
                Datereturnfile.set("80 rupees")
                Sellingprice.set("999")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")

            elif (w == "Castlevania"):
                BookID.set("SBI 0293482736")
                BookTitle.set("Castlevania")
                Author.set("Warren Ellis")
                Datereturnfile.set("70 rupees")
                Sellingprice.set("1999")
                display()

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                Datedue.set(d3)
                Daysonload.set("No")



        listbook = Listbox(listlbl, height=26, width=54, relief=RIDGE,font=("arial", 11, "bold"))
        listbook.bind("<<ListboxSelect>>",selectbook)
        listbook.grid(row=0, column=0, padx=8)
        scrollbar.config(command=listbook.yview)

        for items in listofanimes:
            listbook.insert(END,items)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.txtdisplay=Label(Topframe3,font=("arial", 10, "bold"),text="Member_type\t\tRefrence_No\t\tTitle\t\tFirst_name\t\tSurname\t\tAddress\t\tPost_code\t\tMobile_no\t\tBook_Title\t\tDate_Borrowed",)
        self.txtdisplay.grid(row=0, column=0)


        self.bottomtxt = Text(Topframe3, relief=RIDGE,height=4, width=215,font=("arial", 10, "bold"),padx=4,pady=4)
        self.bottomtxt.grid(row=1, column=0)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        displaybtn=Button(bottomframe,bd=4,text="Display Data",font=("arial",12,"bold"),bg="#c2c2c2",padx=24,fg="#800080",width=8,command=reciept)
        displaybtn.grid(row=0,column=0)

        Deletebtn = Button(bottomframe,bd=4, text="Delete", font=("arial", 12, "bold"), bg="#c2c2c2",fg="#800080",padx=24,width=8,command=Delete)
        Deletebtn.grid(row=0, column=2)

        printbtn = Button(bottomframe, bd=4, text="print", font=("arial", 12, "bold"), bg="#c2c2c2", fg="#800080",
                           padx=24, width=8, command=print)
        printbtn.grid(row=0, column=4)

        Resetbtn = Button(bottomframe, text="Reset",bd=4, font=("arial", 12, "bold"), bg="#c2c2c2",fg="#800080",padx=24,width=8,command=reset)
        Resetbtn.grid(row=0, column=6)

        Exitbtn = Button(bottomframe,bd=4, text="Exit", font=("arial", 12, "bold"), bg="#c2c2c2",fg="#800080",padx=24,width=8,command=exit)
        Exitbtn.grid(row=0, column=8)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__ == "__main__":
    madara=Tk()
    application=Library(madara)
    madara.mainloop()