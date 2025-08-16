from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk


window_employee = Toplevel()
window_employee.title("Add New Employee")
window_employee.iconbitmap("D:\\SMI\\SMI1.ico")
window_employee.geometry("700x700")
window_employee.resizable(0,0)
window_employee.state("zoomed")

bg_frame = Image.open("D:\\SMI\\Images\\background1.png")
bg_photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window_employee, image = bg_photo)
bg_panel.image = bg_photo
bg_panel.pack(fill = "both", expand = "yes")


def submit():
    if id_entry.get() == "" or name_entry.get() == "" or email_entry.get() == "" or phone_entry.get() == "":
        messagebox.showerror("Error","All fields are required")
    elif id_entry.get().isnumeric() == False:
        messagebox.showerror("Error","Id must be a number")
    elif name_entry.get().isnumeric() == True:
        messagebox.showerror("Error","Name must be a string")
    elif phone_entry.get().isnumeric() == False or len(phone_entry.get()) != 10:
        messagebox.showerror("Error","Invalid Phone Number")
    elif aadhar_entry.get().isnumeric() == False or len(aadhar_entry.get()) != 12:
        messagebox.showerror("Error","Aadhar Card Number must be of 12 digit")
    else:
        try:
            conn = pymysql.connect(host = "localhost",user = "root", password = "pihu123")
            mycursor = conn.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue, Try Again")
            return
        try:
            query = "create database employees"
            mycursor.execute(query)
            query = "use employees"
            mycursor.execute(query)
            query = "create table employee(id int, name varchar(50), email varchar(50), phone_number varchar(50), aadhar_no varchar(20), address varchar(200))"
            mycursor.execute(query)
        except:
            mycursor.execute("use employees")   

        query = "select * from employee where id = %s"
        mycursor.execute(query,(id_entry.get()))

        row = mycursor.fetchone()

        if row != None:
            messagebox.showerror("Error", "This Employee Id Already Exists")   
        else:
            query = "insert into employee(id,name,email,phone_number,aadhar_no,address) values(%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,(id_entry.get(),name_entry.get(),email_entry.get(),phone_entry.get(),aadhar_entry.get(),address_entry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Employee registered successfully!!!")

def clear():
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    phone_entry.delete(0,END)
    aadhar_entry.delete(0,END)
    address_entry.delete(0,END)  

def back():
    window_employee.iconify()

main_frame = Frame(window_employee, width = 900, height = 720, bg = "white") 
main_frame.place(x = 250, y = 10)

new_employee_lbl = Label(window_employee, text = "NEW EMPLOYEE DETAILS", bg = "white",fg = "#00337C",font = ("yu gothic ui",30,"bold"))
new_employee_lbl.place(x = 480, y = 20)

id_label = Label(window_employee, text = "Employee Id", font = ("yu gothic ui",13,"bold"), bg = "white", fg = "#00337C")
id_label.place(x = 450, y = 115)

id_entry = Entry(window_employee,font = ("yu gothic ui",12,"bold"),bg = "#00337C", fg = "white",width = 51)
id_entry.place(x = 455, y = 150)

name_label = Label(window_employee, text = "Employee Name", font = ("yu gothic ui",13,"bold"), bg = "white", fg = "#00337C")
name_label.place(x = 450, y = 195)

name_entry = Entry(window_employee,font = ("yu gothic ui",12,"bold"),bg = "#00337C", fg = "white",width = 51)
name_entry.place(x = 455, y = 230)

email_label = Label(window_employee, text = "Employee Email", font = ("yu gothic ui",13,"bold"), bg = "white", fg = "#00337C")
email_label.place(x = 450, y = 275)

email_entry = Entry(window_employee,font = ("yu gothic ui",12,"bold"),bg = "#00337C", fg = "white",width = 51)
email_entry.place(x = 455, y = 310)

phone_label = Label(window_employee, text = "Employee Phone Number", font = ("yu gothic ui",13,"bold"), bg = "white", fg = "#00337C")
phone_label.place(x = 450, y = 355)

phone_entry = Entry(window_employee,font = ("yu gothic ui",12,"bold"),bg = "#00337C", fg = "white",width = 51)
phone_entry.place(x = 455, y = 390)

aadhar_label = Label(window_employee, text = "Employee Aadhar Card No.", font = ("yu gothic ui",13,"bold"), bg = "white", fg = "#00337C")
aadhar_label.place(x = 450, y = 435)

aadhar_entry = Entry(window_employee,font = ("yu gothic ui",12,"bold"),bg = "#00337C", fg = "white",width = 51)
aadhar_entry.place(x = 455, y = 470)

address_label = Label(window_employee, text = "Employee Address", font = ("yu gothic ui",13,"bold"), bg = "white", fg = "#00337C")
address_label.place(x = 450, y = 515)

address_entry = Entry(window_employee,font = ("yu gothic ui",12,"bold"),bg = "#00337C", fg = "white",width = 51)
address_entry.place(x = 455, y = 550)

submit_button = Button(window_employee, text = "SUBMIT", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = submit)
submit_button.place(x = 530, y = 610)

clear_button = Button(window_employee, text = "CLEAR", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = clear)
clear_button.place(x = 710, y = 610)

back_button = Button(window_employee, text = "<-", font = ("yu gothic ui", 27, "bold"), fg = "#00337C", bg = "white", width = 2, cursor="hand2",command = back, bd = 0)
back_button.place(x = 290, y = 10)
