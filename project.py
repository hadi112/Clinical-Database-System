###CREATED BY HADI HUSAIN###
#! python2
import sqlite3
from Tkinter import *
from tkMessageBox import *
#from google import *
import datetime
import webbrowser
root=Tk()
root.title("CLINIC SYSTEM")

#icon=PhotoImage(file="source.gif")
#Label(root,image=icon).place(rely=0.000012)

#########DATABASE############
connection=sqlite3.connect("medicine.db")
cur=connection.cursor()
cur.execute("create table if not exists clinicdb(disease varchar(30) primary key,drugs varchar(60),dosage_adult  varchar(70),dosage_kid varchar(70))")
cur.execute("create table if not exists records(disease varchar (30) ,patient_name char(30),patient_age number,date varchar(20))")
cur.execute("select * from clinicdb")
for row in cur.fetchall():
    print (row[0])
connection.commit()

#############FUNCTIONS###############
def medi(): 
    try:  
        if int(b.get())>18:
            root4=Toplevel()
            root4.title("PRESCRIPTION")
            root4.geometry('400x300')
            a=c.get()
            cur.execute("select drugs,dosage_adult from clinicdb where disease=(?)",[a])
            z=cur.fetchall()
            Label(root4,text="Drug:",font="times 20 bold",justify="center").grid(row=0,column=1)
            Label(root4,text= z[0][0],font="times 20 bold").grid(row=1,column=1)
            Label(root4,text="\n").grid(row=2,column=1)
            Label(root4,text="Dosage:",font="times 20 bold",justify="center").grid(row=3,column=1)
            Label(root4,text= z[0][1],font="times 20 bold").grid(row=4,column=1)
            clear()
            root4.mainloop()
        else:
            root5=Toplevel()
            root5.title("PRESCRIPTION")
            root5.geometry('400x300')
            v=c.get()
            cur.execute("select drugs,dosage_kid from clinicdb where disease=(?)",[v])
            x=cur.fetchall()
            Label(root5,text="Drugs:",font="times 20 bold",justify="center").grid(row=0,column=1)
            Label(root5,text= x[0][0],font="times 20 bold").grid(row=1,column=1)
            Label(root5,text="\n").grid(row=2,column=1)
            Label(root5,text="Dosage:",font="times 20 bold",justify="center").grid(row=3,column=1)
            Label(root5,text= x[0][1],font="times 20 bold").grid(row=4,column=1)
            clear()
            root5.mainloop()
    except IndexError:
        clear()
        showinfo("ATTENTION","!Drugs not found!")
    
def deleteall():
    
    x=askyesno("info","Are You Sure?")
    if(x==True):
        cur.execute("delete from records")
        connection.commit()
        showinfo("Done","All Records have been Sucessfully Deleted")
    elif(x==False):
        showinfo("Done","No Records are Deleted")
        

def submit():
    if c.get()=="" or a.get()=="" or b.get()=="" or d.get()=="":
         showerror("Error","Missing Fields")
    else:
        cur.execute("insert into records values(?,?,?,?)",(c.get(),a.get(),b.get(),d.get()))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        connection.commit()
        medi()


def records():
    root3=Toplevel()
    root3.title("RECORDS")
    cur.execute("select * from records")
    z=cur.fetchall()
    length=len(z)
    Label(root3,text="Patients Records\n",font="times 20 bold",).grid(row=0,column=0,columnspan=4)
    for i in range(length):
        Label(root3,font="times 12 bold",text="Diesease: "+str(z[i][0])).grid(row=i+1,column=0,sticky=N)
        Label(root3,font="times 12 bold",text="Patient Name: "+str(z[i][1])).grid(row=i+1,column=1,sticky=N)
        Label(root3,font="times 12 bold",text="Patient age: "+str(z[i][2])).grid(row=i+1,column=2,sticky=N)
        Label(root3,font="times 12 bold",text="Date: "+str(z[i][3])).grid(row=i+1,column=3,sticky=N)        
    root3.mainloop()

def callback(event):
     webbrowser.open_new("https:\\www.google.com")
    

def moreinfo():
    root2=Toplevel()
    root2.title("MORE INFO")
    query=c.get() + "remedies"
    for j in search(query,tld="co.in",num=15,stop=1,pause=2):
        link=Label(root2,text= j , fg="red", cursor="hand2")
        link.pack()
        link.bind("<Button-1>",callback )


def clear():
    a.delete(0,END)
    b.delete(0,END)
    c.delete(0,END)
    d.delete(0,END)
    d.insert(0,today)

                           
def About():
    root1=Toplevel()
    root1.title("About Developer")
    Label(root1,text="This project is made by Hadi Husain \
                      Enrollment No.=161B118",font='times 15 bold').grid(row=1)


def help1():
    showinfo("HELP","""        Click SUBMIT to get medicine.
        Click Records to see previous patients records.
        Click Clear to empty the Entry fields.
        OD and BDS stand for once a day and 2 times a day\n""")


today=datetime.date.today()

def update():
    cur.execute("update records set ")


########LABELS#############
Label(root,text='CLINICAL DATABASE SYSTEM',font='times 20 bold',bd=6,relief='ridge',bg='powder blue').grid(row=0,columnspan=4)
Label(root,text='Patient Name',font='comic 10 bold',bd=6,relief="ridge").grid(row=2,column=0)
a=Entry(root)
a.grid(row=2,column=1)
Label(root,text='Patient Age',font='comic 10 bold',bd=6,relief="ridge").grid(row=3,column=0)
b=Entry(root)
b.grid(row=3,column=1)
Label(root,text='Disease',font='comic 10 bold',bd=6,relief="ridge").grid(row=4,column=0)
c=Entry(root)
c.grid(row=4,column=1)
Label(root,text='Date',font='comic 10 bold',bd=6,relief="ridge").grid(row=5,column=0)
d=Entry(root)
d.grid(row=5,column=1)
d.insert(0,today)

########BUTTONS############
Button(root,text='SUBMIT',font='comic 10 bold',bd=6,bg='cyan2',command=submit).grid(row=6,column=1)
Button(root,text='Help',font='comic 10 bold',bd=6,bg='red',command=help1).grid(row=5,column=3)
Button(root,text='Delete All',font='comic 10 bold',bd=6,bg='green2',command=deleteall).grid(row=6,column=0)
Button(root,text='About Developer',font='comic 10 bold',bd=6,bg='orange',command=About).grid(row=1,column=0)
Button(root,text='Records',font='comic 10 bold',bd=6,bg='yellow',command=records).grid(row=1,column=1)
Button(root,text='CLEAR',font='comic 10 bold',bd=6,bg='orange',command=clear).grid(row=1,column=3)
Button(root,text='More Info',font='comic 10 bold',bd=6,bg='powder blue',command=moreinfo).grid(row=3,column=3)
Button(root,text='scrapy',font='comic 10 bold',bd=6,bg='powder blue').grid(row=6,column=3)


root.mainloop()
