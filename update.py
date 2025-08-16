from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
from tkinter import ttk

window_employee = Toplevel()
window_employee.title("Update Employee Details")
window_employee.iconbitmap("D:\\SMI\\SMI1.ico")
window_employee.geometry("700x700")
window_employee.resizable(0,0)
window_employee.state("zoomed")

bg_frame = Image.open("D:\\SMI\\Images\\background1.png")
bg_photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window_employee, image = bg_photo)
bg_panel.image = bg_photo
bg_panel.pack(fill = "both", expand = "yes")


def callback(*args):
    id = n.get()
    try:
        conn = pymysql.connect(host = "localhost",user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")

    mycursor.execute("use employees")  

    query = "select * from employee where id = %s"
    mycursor.execute(query,(id))

    rows = mycursor.fetchone()
    name_entry.insert(0,rows[1])
    email_entry.insert(0,rows[2])
    phone_entry.insert(0,rows[3])
    aadhar_entry.insert(0,rows[4])
    address_entry.insert(0,rows[5])


def set_combo_box():
    try:
        conn = pymysql.connect(host = "localhost",user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")

    mycursor.execute("use employees")  

    query = "select id from employee"
    mycursor.execute(query)

    row = mycursor.fetchall()

    id_combo_box["values"] = row



def update():
    if id_combo_box.get() == "":
        messagebox.showerror("Error","Please Select An Employee Id")
    else:
        try:
            conn = pymysql.connect(host = "localhost",user = "root", password = "pihu123")
            mycursor = conn.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        
        mycursor.execute("use employees")

        query = "update employee set name = %s, email = %s, phone_number = %s, aadhar_no = %s, address = %s where id = %s"
        mycursor.execute(query,(name_entry.get(),email_entry.get(),phone_entry.get(),aadhar_entry.get(),address_entry.get(),n.get()))
        messagebox.showinfo("Success","Employee Details Updated Sucessfully")
        conn.commit()
        conn.close()

def clear():
    name_entry.delete(0,END)
    id_combo_box.delete(0,END)
    email_entry.delete(0,END)
    phone_entry.delete(0,END)
    aadhar_entry.delete(0,END)
    address_entry.delete(0,END)
                
def back():
    window_employee.iconify()

main_frame = Frame(window_employee, width = 900, height = 720, bg = "white") 
main_frame.place(x = 250, y = 10)

new_employee_lbl = Label(window_employee, text = "UPDATE EMPLOYEE DETAILS", bg = "white",fg = "#00337C",font = ("yu gothic ui",30,"bold"))
new_employee_lbl.place(x = 480, y = 20)

id_label = Label(window_employee, text = "Employee Id", font = ("yu gothic ui",13,"bold"), bg = "white", fg = "#00337C")
id_label.place(x = 450, y = 115)

n = StringVar()

id_combo_box = ttk.Combobox(window_employee,width=73,textvariable=n,)
id_combo_box.place(x = 455, y = 150)

n.trace("w",callback)

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


update_button = Button(window_employee, text = "UPDATE", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = update)
update_button.place(x = 540, y = 610)

clear_button = Button(window_employee, text = "CLEAR", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 15, cursor="hand2",command = clear)
clear_button.place(x = 700, y = 610)

back_button = Button(window_employee, text = "<-", font = ("yu gothic ui", 27, "bold"), fg = "#00337C", bg = "white", width = 2, cursor="hand2",command = back, bd = 0)
back_button.place(x = 290, y = 10)

set_combo_box()
