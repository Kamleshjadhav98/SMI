from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import datetime
from datetime import date
from PIL import Image,ImageTk
import calendar
import sys

window = Toplevel()
window.title("In Attendance")
window.geometry("1166x718")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.resizable(0, 0)
window.state("zoomed")

bg_frame = Image.open("D:\\SMI\\Images\\background1.png")
bg_photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window, image = bg_photo)
bg_panel.image = bg_photo
bg_panel.pack(fill = "both", expand = "yes")

def today_day(e):
    current_date = str(sv.get())
    day = datetime.datetime.strptime(current_date, '%Y-%m-%d').weekday()
    day_entry.insert(0,calendar.day_name[day])

def callback(*args):
    id = n.get()

    try:
        conn = pymysql.connect(host = "localhost", user = "root", password="pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        return
    mycursor.execute("use employees")
    
    query = "select * from employee where id = %s"
    mycursor.execute(query,(id))

    row = mycursor.fetchone()
    name_entry.insert(0,row[1])

def callback1():
    sv.get()

def set_combo_box():
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password="pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        return
    mycursor.execute("use employees")

    query = "select id from employee"
    mycursor.execute(query)

    row = mycursor.fetchall()

    emp_id_box["values"] = row

def clear():
    date_entry.delete(0,END)
    day_entry.delete(0,END)
    emp_id_box.delete(0,END)
    name_entry.delete(0,END)
    in_entry.delete(0,END)
    per_hour_wages_entry.delete(0,END)

def insert():

    if date_entry.get() == "" or  day_entry.get() == "" or emp_id_box.get() == "" or name_entry.get() == "" or in_entry.get() == "" or per_hour_wages_entry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
    else:
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
            mycursor = conn.cursor()
        except:
            messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
            print("Hello")
            return
        
        try:
            query = "create database attendances"
            mycursor.execute(query)
            query = "use attendances"
            mycursor.execute(query)
            query = "create table attendance(id int,name varchar(50),date varchar(20),day varchar(20),in_time varchar(20), out_time varchar(20),wages_per_hour int, total_hours_worked varchar(50), total_wages varchar(10),overtime_hours varchar(30),overtime_wages varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("use attendances")
        
        query = "select * from attendance where id = %s and date = %s"
        mycursor.execute(query,(n.get(),sv.get()))

        row = mycursor.fetchone()

        if row == None:
            query = "insert into attendance(id,name,date,day,in_time,out_time,wages_per_hour,total_hours_worked,total_wages,overtime_hours,overtime_wages) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,(n.get(),name_entry.get(),date_entry.get(),day_entry.get(),in_entry.get(),"",per_hour_wages_entry.get(),"","","",""))
            conn.commit()
            conn.close()
            # messagebox.showinfo("Success","Data Inserted Successfully")
        
        else:
            messagebox.showerror("Error","Double entries!!!")

def back():
    window.update()
    window.iconify()

frame = Frame(window, width = 900, height = 720, bg = "white") 
frame.place(x = 250, y = 10)

att_lbl = Label(frame,text = "IN TIME",bg = "white",fg = "#00337C",font = ("yu gothic ui",40,"bold"))
att_lbl.place(x = 350,y = 20)

date_lbl = Label(frame,text = "Date",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
date_lbl.place(x = 220, y = 142)

sv = StringVar()
date_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"),textvariable=sv,validate="focusout",validatecommand=callback1)
date_entry.place(x = 460, y = 150)

date_format_lbl = Label(frame,text = "Enter in this format yyyy-mm-dd For ex. 2023-01-28",bg = "white", fg = "#00337C",font = ("yu gothic ui",12,"bold"))
date_format_lbl.place(x = 458, y = 175)

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

in_lbl = Label(frame,text = "In Time",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
in_lbl.place(x = 220, y = 422)

in_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
in_entry.place(x = 460, y = 430)

in_format_lbl = Label(frame,text = "Enter in this format hh:mm AM/PM For ex. 11:00 AM, 02:00 PM",bg = "white", fg = "#00337C",font = ("yu gothic ui",10,"bold"))
in_format_lbl.place(x = 458, y = 455)

per_hour_wages_lbl = Label(frame,text = "Per Hour Wages",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
per_hour_wages_lbl.place(x = 220, y = 492)

per_hour_wages_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
per_hour_wages_entry.place(x = 460, y = 500)

insert_button = Button(frame, text = "INSERT", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = insert)
insert_button.place(x = 280, y = 600)

clear_button = Button(frame, text = "CLEAR", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = clear)
clear_button.place(x = 460, y = 600)

back_button = Button(frame, text = "<-", font = ("yu gothic ui", 27, "bold"), fg = "#00337C", bg = "white", width = 2, cursor="hand2",command = back, bd = 0)
back_button.place(x = 50, y = 10)

set_combo_box()
