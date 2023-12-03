#Backend code..

import sqlite3

def acadamicdata():
    con=sqlite3.connect("acadamic.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS acadamic(id INTEGER PRIMARY KEY, Name text,Designation text,Qualification text,Date_Of_Joining text,Contact text,Email_ID text,"
                "Research_Guide text,Dare_Of_Registration text,Research_Topic text, Name_Of_Course text,Eligibility text,Durartion text)")
    con.commit()
    con.close()

def addacadamicRec(Name,Designation,Date_Of_Joining,Qualification,Contact,Email_ID,Research_Guide,Date_Of_Registration,Research_Topic,Name_of_Courses,Eligibility,Duration):
    con=sqlite3.connect("acadamic.db")
    cur=con.cursor()
    cur.execute("INSERT INTO acadamic VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)",
    (Name,Designation,Date_Of_Joining,Qualification,Contact,Email_ID,Research_Guide,Date_Of_Registration,Research_Topic,Name_of_Courses,Eligibility,Duration))
    con.commit()
    con.close()

def viewdata():
        con=sqlite3.connect("acadamic.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM acadamic")
        rows=cur.fetchall()
        con.close()
        return rows

def deleteRec():
    con=sqlite3.connect("acadamic.db")
    cur=con.cursor()
    con=cur.execute("DELETE * FROM acadamic WHERE id=?",(id,))
    rows=cur.fetchall()
    con.close()
    return rows

def searchdata(Name="",Designation="",Date_Of_Joining="",Qualification="",Contact="",Email_ID="",Research_Guide="",Date_Of_Registration="",Research_Topic="",Name_of_Courses="",Eligibility="",Duration=""):
    con=sqlite3.connect("acadamic.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM acadamic WHERE Name=? OR Designation=? OR Date_Of_Joining=? OR Qualification=? OR ContactEmail_ID=? OR Research_Guide=? OR Date_Of_Registration=? OR Research_Topic=? OR Name_of_Courses=? OR Eligibility=? OR Duration=?",
    (Name,Designation,Date_Of_Joining,Qualification,Contact,Email_ID,Research_Guide,Date_Of_Registration,Research_Topic,Name_of_Courses,Eligibility,Duration))
    rows =cur.fetchall()
    con.close()
    return rows

def updatedata(Name="",Designation="",Date_Of_Joining="",Qualification="",Contact="",Email_ID="",Research_Guide="",Date_Of_Registration="",Research_Topic="",Name_of_Courses="",Eligibility="",Duration=""):
    con=sqlite3.connect("acadamic.db")
    cur=con.cursor()
    cur.execute("UPDATE acadamic SET Name=?,Designation=?,Date_Of_Joining=?,Qualification=?,ContactEmail_ID=?,Research_Guide=?,Date_Of_Registration=?,Research_Topic=?,Name_of_Courses=?,Eligibility=?,Duration=?",
    (Name,Designation,Date_Of_Joining,Qualification,Contact,Email_ID,Research_Guide,Date_Of_Registration,Research_Topic,Name_of_Courses,Eligibility,Duration,id))
    rows =cur.fetchall()
    con.close()
    return rows

acadamicdata()
