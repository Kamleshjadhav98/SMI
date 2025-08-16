from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from datetime import date
from PIL import Image,ImageTk
import datetime
import calendar

window = Toplevel()
window.title("Over Time")
window.geometry("1166x718")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.resizable(0, 0)
window.state("zoomed")
window.config(bg = "#1C82AD")


def today_day(e):
    current_date = str(sv.get())
    day = datetime.datetime.strptime(current_date, '%Y-%m-%d').weekday()
    day_entry.insert(0,calendar.day_name[day])

def callback(*args):
    n.get()
    sv.get()
    sv1.get()
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password="pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        return
    mycursor.execute("use attendances")
    
    query = "select * from attendance where id = %s and date = %s"
    mycursor.execute(query,(n.get(),sv.get()))

    row = mycursor.fetchone()
    name_entry.insert(0,row[1])
    per_hour_wages_entry.insert(0,row[6])


def set_combo_box():
    date = sv.get()
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password="pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        return
    mycursor.execute("use attendances")

    query = "select id from attendance where date = %s"
    mycursor.execute(query,(date))

    row = mycursor.fetchall()

    emp_id_box["values"] = row

def overtime_hours(*args):
    sv1.get()

def clear():
    date_entry.delete(0,END)
    emp_id_box.delete(0,END)
    day_entry.delete(0,END)
    name_entry.delete(0,END)
    overtime_hours_entry.delete(0,END)
    per_hour_wages_entry.delete(0,END)
    overtime_wages_entry.delete(0,END)

def calculate():
    n.get()
    sv.get()
    sv1.get()
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password="pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        return
    mycursor.execute("use attendances")
    
    query = "select * from attendance where id = %s and date = %s"
    mycursor.execute(query,(n.get(),sv.get()))

    row = mycursor.fetchone()
    time = str(sv1.get())
    hours, mins = map(int,time.split(":"))
    wages = row[6]
    total_wages = "Rs "+ str(((mins / 60) + hours) * wages)
    overtime_wages_entry.insert(0,total_wages)


def insert():
    hours,mins = map(int,overtime_hours_entry.get().split(":"))
    time = f"{hours} hours {mins} mins"
    if date_entry.get() == "" or  day_entry.get() == "" or emp_id_box.get() == "" or name_entry.get() == "" or overtime_hours_entry.get() == "" or per_hour_wages_entry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
    else:
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
            mycursor = conn.cursor()
        except:
            messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
            return
        
        mycursor.execute("use attendances")
        query = "select * from attendance where id = %s and date = %s"
        mycursor.execute(query,(n.get(),sv.get()))

        row = mycursor.fetchone()

        if row != None:
            query = "update attendance set overtime_hours = %s, overtime_wages = %s where id = %s and date = %s"
            mycursor.execute(query,(time,overtime_wages_entry.get(),n.get(),date_entry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Data Inserted Successfully")
        else:
            messagebox.showerror("Error","No such entries!!!")

def back():
    window.iconify()

frame = Frame(window, width = 900, height = 720, bg = "white") 
frame.place(x = 250, y = 10)

att_lbl = Label(frame,text = "OverTime",bg = "white",fg = "#00337C",font = ("yu gothic ui",40,"bold"))
att_lbl.place(x = 330,y = 20)

date_lbl = Label(frame,text = "Date",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
date_lbl.place(x = 220, y = 142)

sv = StringVar()
date_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"),textvariable=sv,validate="focusout",validatecommand=set_combo_box)
date_entry.place(x = 460, y = 150)


day_lbl = Label(frame,text = "Day",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
day_lbl.place(x = 220, y = 212)

day_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
day_entry.place(x = 460, y = 220)

day_entry.bind("<FocusIn>",today_day)

emp_id = Label(frame, text = "Employee Id",bg = "white",fg = "#00337C",font = ("yu gothic ui",19,"bold"))
emp_id.place(x = 220, y = 290)

n = StringVar()
emp_id_box = ttk.Combobox(frame,width=33,textvariable=n)
emp_id_box.place(x = 460,y = 299)

n.trace("w",callback)

name_lbl = Label(frame,text = "Employee Name",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
name_lbl.place(x = 220, y = 352)

name_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
name_entry.place(x = 460, y = 365)

per_hour_wages_lbl = Label(frame,text = "Per Hour Wages",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
per_hour_wages_lbl.place(x = 220, y = 422)

per_hour_wages_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
per_hour_wages_entry.place(x = 460, y = 430)

overtime_hours_lbl = Label(frame,text = "Over Time Hours",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
overtime_hours_lbl.place(x = 220, y = 492)

sv1 = StringVar()

overtime_hours_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"),textvariable=sv1,validate="focusout",validatecommand=overtime_hours)
overtime_hours_entry.place(x = 460, y = 500)

overtime_hours_lbl = Label(frame, text = "Enter in this format hh:mm, For ex. 00:30 or 01:00 or 01:30",bg = "white",fg = "#00337C",font = ("yu gothic ui",11,"bold"))
overtime_hours_lbl.place(x = 455, y = 530)

overtime_wages_lbl = Label(frame,text = "Over Time Wages",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
overtime_wages_lbl.place(x = 220, y = 562)

overtime_wages_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
overtime_wages_entry.place(x = 460, y = 570)


calculate_button = Button(frame, text = "CALCULATE", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = calculate)
calculate_button.place(x = 200, y = 650)

insert_button = Button(frame, text = "INSERT", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = insert)
insert_button.place(x = 380, y = 650)

clear_button = Button(frame, text = "CLEAR", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = clear)
clear_button.place(x = 560, y = 650)

back_button = Button(frame, text = "<-", font = ("yu gothic ui", 27, "bold"), fg = "#00337C", bg = "white", width = 2, cursor="hand2",command = back, bd = 0)
back_button.place(x = 60, y = 10)

set_combo_box()
