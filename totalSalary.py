from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import datetime
from datetime import date
from PIL import Image,ImageTk
import calendar
import re

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
     
def callback1():
    sv1.get()

def callback(*args):
    n.get()
    year, month = map(int,sv1.get().split("-"))
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password="pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        return
    mycursor.execute("use employees")

    query = "select * from employee where id = %s"
    mycursor.execute(query,(n.get()))

    row = mycursor.fetchone()
    name_entry.insert(0,row[1])

    mycursor.execute("use attendances")
    
    query = "select total_wages from attendance where id = %s and MONTH(date) = %s and YEAR(date) = %s"
    mycursor.execute(query,(n.get(),month,year))

    rows = mycursor.fetchall()

    trim = re.compile(r'[^\d.,]+')
    initial_salary_trim = 0
    for i in rows:
        for j in i:
            initial_salary_trim += float(trim.sub('',j))

    initial_salary_entry.insert(0,f"Rs {initial_salary_trim}")

    trim = re.compile(r'[^\d.,]+')
    callback.result = 0
    for i in rows:
        for j in i:
            callback.result += float(trim.sub('', j))

    mycursor.execute("use advances")

    query = "select advance from advance where id = %s and MONTH(date) = %s and YEAR(date) = %s"
    mycursor.execute(query,(n.get(),month,year))

    row1 = mycursor.fetchall()
    callback.total_advance = 0
    for i in row1:
        for j in i:
            callback.total_advance += int(j)
    advance = f"Rs {callback.total_advance}"
    advance_entry.insert(0,advance)


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

def calculate():
    commission = int(commission_entry.get())
    total_commission = ((callback.result / commission) + callback.result) - callback.total_advance
    final_salary = f"Rs {total_commission}"
    final_salary_entry.insert(0,final_salary)

def clear():
    name_entry.delete(0,END)
    advance_entry.delete(0,END)
    emp_id_box.delete(0,END)
    month_year_entry.delete(0,END)
    initial_salary_entry.delete(0,END)
    commission_entry.delete(0,END)
    advance_entry.delete(0,END)
    final_salary_entry.delete(0,END)
def insert():
    commission = commission_entry.get()
    commission_percent = f"{commission} %" 

    if month_year_entry.get() == "" or emp_id_box.get() == "" or name_entry.get() == "" or initial_salary_entry.get() == "" or commission_entry.get() == "" or advance_entry.get() == "" or final_salary_entry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
    else:
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
            mycursor = conn.cursor()
        except:
            messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
            return
        
        try:
            query = "create database final_salary_receipts"
            mycursor.execute(query)
            query = "use final_salary_receipts"
            mycursor.execute(query)
            query = "create table final_salary_receipt(id int,name varchar(50),month_year varchar(30),initial_salary varchar(20),commission varchar(10),advance varchar(20),final_salary varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("use final_salary_receipts")
        
        query = "insert into final_salary_receipt(id,name,month_year,initial_salary,commission,advance,final_salary) values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query,(n.get(),name_entry.get(),month_year_entry.get(),initial_salary_entry.get(),commission_percent,advance_entry.get(),final_salary_entry.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Data inserted successfully")

def back():
    window.iconify()

frame = Frame(window, width = 900, height = 700, bg = "white") 
frame.place(x = 260, y = 30)

att_lbl = Label(frame,text = "TOTAL SALARY",bg = "white",fg = "#00337C",font = ("yu gothic ui",40,"bold"))
att_lbl.place(x = 260,y = 20)

month_year_lbl = Label(frame,text = "Month & Year",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
month_year_lbl.place(x = 220, y = 142)

sv1 = StringVar()
month_year_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"),textvariable=sv1,validate="focusout",validatecommand=callback1)
month_year_entry.place(x = 460, y = 151)


month_year_format_lbl = Label(frame,text = "For ex. 2023-01",bg = "white", fg = "#00337C",font = ("yu gothic ui",12,"bold"))
month_year_format_lbl.place(x = 460, y = 176)

emp_id_lbl = Label(frame, text = "Employee Id",bg = "white",fg = "#00337C",font = ("yu gothic ui",19,"bold"))
emp_id_lbl.place(x = 220, y = 212)

n = StringVar()
emp_id_box = ttk.Combobox(frame,width=33,textvariable=n)
emp_id_box.place(x = 460,y = 220)


name_lbl = Label(frame,text = "Employee Name",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
name_lbl.place(x = 220, y = 283)

name_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
name_entry.place(x = 460, y = 291)

initial_salary_lbl = Label(frame,text = "Initial Salary",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
initial_salary_lbl.place(x = 220, y = 354)

initial_salary_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
initial_salary_entry.place(x = 460, y = 361)

commission_lbl = Label(frame,text = "Commission",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
commission_lbl.place(x = 220, y = 417)

commission_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
commission_entry.place(x = 460, y = 425)

n.trace("w",callback)
advance_lbl = Label(frame,text = "Advance",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
advance_lbl.place(x = 220, y = 480)

advance_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
advance_entry.place(x = 460, y = 488)

final_salary_lbl = Label(frame,text = "Final Salary",bg = "white", fg = "#00337C",font = ("yu gothic ui",19,"bold"))
final_salary_lbl.place(x = 220, y = 551)

final_salary_entry = Entry(frame,bg = "#00337C",fg = "white",width=24, font = ("yu gothic ui",12,"bold"))
final_salary_entry.place(x = 460, y = 559)

calculate_button = Button(frame, text = "CALCULATE", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = calculate)
calculate_button.place(x = 200, y = 630)

insert_button = Button(frame, text = "INSERT", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = insert)
insert_button.place(x = 380, y = 630)

clear_button = Button(frame, text = "CLEAR", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = clear)
clear_button.place(x = 560, y = 630)

back_button = Button(frame, text = "<-", font = ("yu gothic ui", 27, "bold"), fg = "#00337C", bg = "white", width = 2, cursor="hand2",command = back, bd = 0)
back_button.place(x = 60, y = 10)

set_combo_box()
