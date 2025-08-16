from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from datetime import date
import datetime
from PIL import Image, ImageTk
import calendar
import sys

window = Toplevel()
window.title("Out Attendance")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.config(bg = "#00337C")
window.geometry("1166x718")
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
    sv.get()
    n.get()
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
    
    mycursor.execute("use attendances")

    query = "select * from attendance where id = %s and date = %s"
    mycursor.execute(query,(n.get(),sv.get()))

    rows = mycursor.fetchone()

    name_entry.insert(0,rows[1])
    in_entry.insert(0,rows[4])
    per_hour_wages_entry.insert(0,rows[6])

 
    
def callback1():
    sv1.get()


def out_time(e):
    now = datetime.datetime.now()
    current_time = str(now.strftime("%I:%M %p"))
    out_entry.insert(0,current_time)


def set_combo_box():
    date = sv.get()
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
    
    mycursor.execute("use attendances")

    query = "select id from attendance where date = %s"
    mycursor.execute(query,(date))

    row = mycursor.fetchall()
    emp_id_box["values"] = row

def calculate():
    n.get()
    sv.get()
    sv1.get()
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
    
    mycursor.execute("use attendances")

    query = "select * from attendance where id = %s and date = %s"
    mycursor.execute(query,(n.get(),sv.get()))

    rows = mycursor.fetchone()

    time_in_str = str(rows[4])
    date_in_str = str(rows[2])
    form = "%Y-%m-%d %I:%M %p"
    d1_joint = " ".join([date_in_str , time_in_str])
    d2_joint = " ".join([date_in_str, sv1.get()])
    d1 = datetime.datetime.strptime(d1_joint,form)
    d2 = datetime.datetime.strptime(d2_joint,form)
    diff = str(d2 - d1)
    hours, mins, secs = map(int,diff.split(":"))
    text = f"{hours} hours {mins} mins"
    total_working_hour_entry.insert(0,text)
    per_hour_wages = rows[6]
    wages = (((mins / 60) + hours) * per_hour_wages)
    text = f"Rs {wages}"
    total_wages_entry.insert(0,text)

def insert():
    if date_entry.get() == "" or day_entry.get() == "" or emp_id_box.get() == "" or out_entry == "" or total_working_hour_entry.get() == "" or total_wages_entry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
    else:
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password="pihu123")
            mycursor = conn.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        
        mycursor.execute("use attendances")

        query = "select * from attendance where id = %s and date = %s"
        mycursor.execute(query,(n.get(),sv.get()))

        row = mycursor.fetchone()

        if row[5] == "" or row[6] == "" or row[7] == "":
 
            query = "update attendance set out_time = %s, total_hours_worked = %s, total_wages = %s where id = %s and date = %s"
            mycursor.execute(query,(out_entry.get(),total_working_hour_entry.get(),total_wages_entry.get(),n.get(),sv.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Data Inserted Successfully")
        else:
            messagebox.showerror("Error","Double entries!!!")


def clear():
    date_entry.delete(0,END)
    day_entry.delete(0,END)
    emp_id_box.delete(0,END)
    name_entry.delete(0,END)
    in_entry.delete(0,END)
    out_entry.delete(0,END)
    per_hour_wages_entry.delete(0,END)
    total_working_hour_entry.delete(0,END)
    total_wages_entry.delete(0,END)

def back():
    window.update()
    window.iconify()


frame = Frame(window, width = 900, height = 720, bg = "white") 
frame.place(x = 250, y = 10)

att_lbl = Label(frame,text = "OUT TIME",bg = "white",fg = "#00337C",font = ("yu gothic ui",40,"bold"))
att_lbl.place(x = 320,y = 10)

date_lbl = Label(frame,text = "Date",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
date_lbl.place(x = 220, y = 110)

sv = StringVar()
date_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"), textvariable=sv,validate="focusout",validatecommand=set_combo_box)
date_entry.place(x = 490, y = 110)

date_format_lbl = Label(frame,text = "Enter in this format yyyy-mm-dd For ex. 2023-01-28",bg = "white", fg = "#00337C",font = ("yu gothic ui",10,"bold"))
date_format_lbl.place(x = 488, y = 135)

day_lbl = Label(frame,text = "Day",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
day_lbl.place(x = 220, y = 160)

day_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
day_entry.place(x = 490, y = 170)

day_entry.bind("<FocusIn>",today_day)

emp_id = Label(frame, text = "Employee Id",bg = "white",fg = "#00337C",font = ("yu gothic ui",19,"bold"))
emp_id.place(x = 220, y = 220)

n = StringVar()
emp_id_box = ttk.Combobox(frame,width=33,textvariable=n)
emp_id_box.place(x = 490,y = 229)

n.trace("w",callback)

name_lbl = Label(frame,text = "Employee Name",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
name_lbl.place(x = 220, y = 280)

name_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
name_entry.place(x = 490, y = 289)

in_lbl = Label(frame,text = "In Time",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
in_lbl.place(x = 220, y = 340)

in_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
in_entry.place(x = 490, y = 349)


out_lbl = Label(frame,text = "Out Time",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
out_lbl.place(x = 220, y = 400)

sv1 = StringVar()
out_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"),textvariable=sv1,validate="focusout",validatecommand=callback1)
out_entry.place(x = 490, y = 409)

out_format_lbl = Label(frame,text = "Enter in this format hh:mm AM/PM For ex. 11:00 AM, 02:00 PM",bg = "white", fg = "#00337C",font = ("yu gothic ui",10,"bold"))
out_format_lbl.place(x = 486, y = 434)

per_hour_wages_lbl = Label(frame,text = "Per Hour Wages",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
per_hour_wages_lbl.place(x = 220, y = 460)

per_hour_wages_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
per_hour_wages_entry.place(x = 490, y = 469)


total_working_hour_lbl = Label(frame,text = "Total Hours Worked",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
total_working_hour_lbl.place(x = 220, y = 520)

total_working_hour_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
total_working_hour_entry.place(x = 490, y = 529)


total_wages_lbl = Label(frame,text = "Total Wages",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
total_wages_lbl.place(x = 220, y = 580)

total_wages_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
total_wages_entry.place(x = 490, y = 589)


calculate_button = Button(frame, text = "CALCULATE", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = calculate)
calculate_button.place(x = 200, y = 650)

insert_button = Button(frame, text = "INSERT", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = insert)
insert_button.place(x = 380, y = 650)

clear_button = Button(frame, text = "CLEAR", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = clear)
clear_button.place(x = 560, y = 650)

back_button = Button(frame, text = "<-", font = ("yu gothic ui", 27, "bold"), fg = "#00337C", bg = "white", width = 2, cursor="hand2",command = back, bd = 0)
back_button.place(x = 50, y = 10)
