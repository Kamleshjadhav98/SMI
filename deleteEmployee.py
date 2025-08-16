from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk

window = Toplevel()
window.title("Delete Employees")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.resizable(0,0)
width = 500
height = 300
x = (window.winfo_screenwidth()//2) - (width // 2)
y = (window.winfo_screenheight()//2) - (height // 2)

window.geometry("{}x{}+{}+{}".format(width,height,x,y))

window.config(bg = "#1C82AD")

def callback(*args):
    n.get()

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
    id_combo_box["values"] = (row)

def delete():
    n.get()
    try:
        conn = pymysql.connect(host = "localhost",user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error","Database Connectivity Issue, Try Again")

    mycursor.execute("use employees")

    query = "delete from employee where id = %s"
    mycursor.execute(query,(n.get()))

    mycursor.execute("use attendances")

    query = "delete from attendance where id = %s"
    mycursor.execute(query,(n.get()))

    mycursor.execute("use advances")

    query = "delete from advance where id = %s"
    mycursor.execute(query,(n.get()))

    mycursor.execute("use final_salary_receipts")

    query = "delete from final_salary_receipt where id = %s"
    mycursor.execute(query,(n.get()))
  
    conn.commit()
    conn.close()
    messagebox.showinfo("Success","Data deleted successfully")
    window.iconify()

view_employee_lbl = Label(window,text = "DELETE EMPLOYEE DETAILS",bg = "#1C82AD", fg = "White",font = ("yu gothic ui",23,"bold"))
view_employee_lbl.place(x = 60,y = 20)

search_employee_lbl = Label(window,text = "Enter Employee Id",bg = "#1C82AD", fg = "White",font = ("yu gothic ui",16,"bold"))
search_employee_lbl.place(x = 55,y = 115)

n = StringVar()

id_combo_box = ttk.Combobox(window,width=25,textvariable=n,)
id_combo_box.place(x = 255, y = 124)

n.trace("w",callback)

submit_button = Button(window, text = "DELETE", font = ("yu gothic ui", 12, "bold"), fg = "#1C82AD", bg = "white", width = 13, cursor="hand2",command = delete)
submit_button.place(x = 180, y = 200)

set_combo_box()

