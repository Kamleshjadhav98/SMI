from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk

window_view_employee = Toplevel()
window_view_employee.title("View Employees")
window_view_employee.resizable(0,0)
width = 500
height = 300
x = (window_view_employee.winfo_screenwidth()//2) - (width // 2)
y = (window_view_employee.winfo_screenheight()//2) - (height // 2)

window_view_employee.geometry("{}x{}+{}+{}".format(width,height,x,y))

window_view_employee.config(bg = "#1C82AD")

def callback(*args):
    id = n.get()


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



def search():
    if id_combo_box.get() == "":
        messagebox.showerror("Error", "Please Enter Employee Id")
    else:
        try:
            conn = pymysql.connect(host = "localhost",user = "root", password = "pihu123")
            mycursor = conn.cursor()
        except:
            messagebox.showerror("Error","Database Connectivity Issue, Try Again")
            return
    
        mycursor.execute("use employees")   
        
        query = "select * from employee where id = %s"
        mycursor.execute(query,(n.get()))

        row = mycursor.fetchone()
    

        if row == None:
            messagebox.showerror("Error","Employee with Id doesn't exists")
        else:
            window_view_employee.iconify()
            window_employee_details = Tk()
            window_employee_details.title("Employee Details")

            width = 950
            height = 600
            x = (window_employee_details.winfo_screenwidth()//2) - (width // 2)
            y = (window_employee_details.winfo_screenheight()//2) - (height // 2)

            window_employee_details.geometry("{}x{}+{}+{}".format(width,height,x,y))
            window_employee_details.wm_attributes("-topmost", True)
            window_employee_details.resizable(0,0)
            window_employee_details.config(bg = "#1C82AD")

            details_label = Label(window_employee_details,text = "EMPLOYEE DETAILS", font = ("yu gothic ui",35,"bold"),bg = "#1C82AD",fg = "white")
            details_label.place(x = 310, y = 20)

            id_detail_lbl = Label(window_employee_details,text = "Employee Id:", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            id_detail_lbl.place(x = 115, y = 140)

            id_detail = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            id_detail.place(x = 475, y = 140)

            name_detail_lbl = Label(window_employee_details,text = "Employee Name:", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            name_detail_lbl.place(x = 115, y = 200)

            name_detail = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            name_detail.place(x = 475, y = 200)

            email_detail_lbl = Label(window_employee_details,text = "Employee Email:", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            email_detail_lbl.place(x = 115, y = 260)

            email_detail = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            email_detail.place(x = 475, y = 260)

            phone_detail_lbl = Label(window_employee_details,text = "Employee Phone Number:", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            phone_detail_lbl.place(x = 115, y = 320)

            phone_detail = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            phone_detail.place(x = 475, y = 320)

            aadhar_detail_lbl = Label(window_employee_details,text = "Employee Aadhar No.:", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            aadhar_detail_lbl.place(x = 115, y = 380)

            aadhar_detail = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            aadhar_detail.place(x = 475, y = 380)

            address_detail_lbl = Label(window_employee_details,text = "Employee Address:", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            address_detail_lbl.place(x = 115, y = 440)
                
            address_detail = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            address_detail.place(x = 475, y = 440)

            address_detail2 = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            address_detail2.place(x = 475, y = 480)

            address_detail3 = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            address_detail3.place(x = 475, y = 520)

            address_detail4 = Label(window_employee_details,text = "", bg = "#1C82AD", fg = "white",font = ("yu gothic ui",16,"bold"))
            address_detail4.place(x = 475, y = 560)
            

            id_detail.config(text = row[0])
            name_detail.config(text = row[1])
            email_detail.config(text = row[2])
            phone_detail.config(text = row[3])
            aadhar_detail.config(text = row[4])
            address_detail.config(text = (row[5][:38] + "-"))
            address_detail2.config(text = (row[5][38:85] + "-"))
            address_detail3.config(text = (row[5][85:130]))
            address_detail4.config(text = (row[5][130:]))
            


view_employee_lbl = Label(window_view_employee,text = "VIEW EMPLOYEE DETAILS",bg = "#1C82AD", fg = "White",font = ("yu gothic ui",23,"bold"))
view_employee_lbl.place(x = 70,y = 20)

search_employee_lbl = Label(window_view_employee,text = "Enter Employee Id",bg = "#1C82AD", fg = "White",font = ("yu gothic ui",16,"bold"))
search_employee_lbl.place(x = 55,y = 115)

n = StringVar()

id_combo_box = ttk.Combobox(window_view_employee,width=25,textvariable=n,)
id_combo_box.place(x = 255, y = 124)

n.trace("w",callback)

submit_button = Button(window_view_employee, text = "SEARCH", font = ("yu gothic ui", 12, "bold"), fg = "#1C82AD", bg = "white", width = 13, cursor="hand2",command = search)
submit_button.place(x = 185, y = 200)



set_combo_box()
