from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import datetime
from datetime import date
from PIL import Image,ImageTk
import calendar


window = Toplevel()
window.title("Advance")
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
    emp_id_box.delete(0,END)
    day_entry.delete(0,END)
    name_entry.delete(0,END)
    advance_entry.delete(0,END)

def insert():
    n.get()
    sv.get()
    if date_entry.get() == "" or  day_entry.get() == "" or emp_id_box.get() == "" or name_entry.get() == "" or advance_entry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
    else:
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
            mycursor = conn.cursor()
        except:
            messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
            return
        
        try:
            query = "create database advances"
            mycursor.execute(query)
            query = "use advances"
            mycursor.execute(query)
            query = "create table advance(id int,name varchar(50),date varchar(20),day varchar(20),advance varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("use advances")
        
        query = "insert into advance(id,name,date,day,advance) values(%s,%s,%s,%s,%s)"
        mycursor.execute(query,(n.get(),name_entry.get(),sv.get(),day_entry.get(),advance_entry.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Data inserted successfully")

def back():
    window.iconify()

frame = Frame(window, width = 900, height = 600, bg = "white") 
frame.place(x = 260, y = 70)

att_lbl = Label(frame,text = "ADVANCE",bg = "white",fg = "#00337C",font = ("yu gothic ui",40,"bold"))
att_lbl.place(x = 320,y = 20)

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

advance_lbl = Label(frame,text = "Advance",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
advance_lbl.place(x = 220, y = 422)

advance_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
advance_entry.place(x = 460, y = 430)

insert_button = Button(frame, text = "INSERT", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = insert)
insert_button.place(x = 280, y = 500)

clear_button = Button(frame, text = "CLEAR", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = clear)
clear_button.place(x = 460, y = 500)


back_button = Button(frame, text = "<-", font = ("yu gothic ui", 27, "bold"), fg = "#00337C", bg = "white", width = 2, cursor="hand2",command = back, bd = 0)
back_button.place(x = 60, y = 10)

set_combo_box()
