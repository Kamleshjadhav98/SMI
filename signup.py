from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

                
window = Tk()
window.title("SIGNUP")
window.iconbitmap("D:\\SMI\\SMI1.ico") 
window.geometry("1166x178")
window.state("zoomed")
window.resizable(0, 0)

bg_frame = Image.open("D:\\SMI\\Images\\background1.png")
bg_photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window, image = bg_photo)
bg_panel.image = bg_photo
bg_panel.pack(fill = "both", expand = "yes")

def show():
        hide_button_label = Button(frame, image = photo1, bg = "#EEEEEE", activebackground = "#EEEEEE", cursor = "hand2", bd = 0,command = hide)
        hide_button_label.image = photo1
        hide_button_label.place(x = 322, y = 240)
        password_entry.config(show = '')
        confirm_password_entry.config(show = '')
                
def hide():
        show_button_label = Button(frame, image = photo2, bg = "#EEEEEE", activebackground = "#EEEEEE", cursor = "hand2", bd = 0, command = show)
        show_button_label.image = photo2
        show_button_label.place(x = 322, y = 240)
        password_entry.config(show = "*")
        confirm_password_entry.config(show = "*")

def clear():
        email_entry.delete(0,END)
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        confirm_password_entry.delete(0,END)
        check.set(0)
        window.destroy()
        import login

def connect_database():


        if email_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '' or confirm_password_entry.get() == '':
                messagebox.showerror("Error", "All Fields Are Required")      
        
        elif password_entry.get() != confirm_password_entry.get():
                messagebox.showerror("Error", "Password Mismatched")

        elif check.get() == 0:
                messagebox.showerror("Error" , "Please Accept Terms & Conditions")
        
        else:
                try:
                        conn = pymysql.connect(host = "localhost", user = "root" , password = "pihu123")
                        mycursor = conn.cursor()


                except:
                        messagebox.showerror("Error", "Database Connectivity Issue, Please Try Again")    
                        return 

                try:
                        query = "create database employeedata"
                        mycursor.execute(query)  
                        query = "use employeedata"
                        mycursor.execute(query)
                        query = "create table employee(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))"
                        mycursor.execute(query) 

                except:
                        mycursor.execute("use employeedata")
                
                
                query = "select * from employee where username = %s"
                mycursor.execute(query,(username_entry.get()))

                row = mycursor.fetchone()

                if row != None:
                        messagebox.showerror("Error", "Username Already Exists")

                else:        
                
                        query = "insert into employee(email, username, password) values(%s,%s,%s)"
                        mycursor.execute(query,(email_entry.get(), username_entry.get(), password_entry.get()))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success", "Registration is Successful")
                        clear()

                ################## Main Frame ##################

signup_frame = Frame(window, width=900, height = 600, bg = "white")
signup_frame.place(x = 200, y = 70)

                ################## Welcome label ##################

heading = Label(signup_frame, text = "WELCOME", font = ("yu gothic ui", 25, "bold"), bg = "white", fg = "#00337C")
heading.place(x = 70, y = 30, width = 300, height = 30)
                

                ################## SMI Image ##################

side_left = Image.open("D:\\SMI\\Images\\SMI1.png")
photo = ImageTk.PhotoImage(side_left)
side_image_label = Label(signup_frame, image = photo, bg = "white")
side_image_label.image = photo
side_image_label.place(x = 70, y = 100)


                ################## SMI name label ##################

name_lbl = Label(signup_frame, text = "SHRI MAHESHWARI INDUSTRIES" , font = ("yu gothic ui", 17 , "bold"), fg = "#000B49", bg = "white")
name_lbl.place(x = 50, y = 520)


                ################## Details frame ##################

frame = Frame(signup_frame, width = 350, height = 500, bg = "#EEEEEE")
frame.place(x = 510, y = 50)
                

                ################## User Signup label ##################

userSignup = Label(frame , text = "CREATE AN ACCOUNT" , font = ("yu gothic ui" , 21, "bold"), bg = "#EEEEEE", fg = "#00337C")
userSignup.place(x = 32, y = 15)


                ################## Email label and enrty ##################

email_label = Label(frame, text = "Email", font = ("yu gothic ui",13,"bold"), bg = "#EEEEEE", fg = "#00337C")
email_label.place(x = 40, y = 80)

email_entry = Entry(frame,font = ("yu gothic ui",12,"bold"),bg = "#00337C", fg = "white",width = 30)
email_entry.place(x = 45, y = 110)

                ################## Username label and enrty ##################

username_label = Label(frame, text = "Username", font = ("yu gothic ui",12,"bold"), bg = "#EEEEEE", fg = "#00337C")
username_label.place(x = 40, y = 145)

username_entry = Entry(frame,font = ("yu gothic ui",13,"bold"),bg = "#00337C", fg = "white",width = 30)
username_entry.place(x = 45, y = 175)

                ################## Paswword label and enrty ##################

password_label = Label(frame, text = "Password", font = ("yu gothic ui",12,"bold"), bg = "#EEEEEE", fg = "#00337C")
password_label.place(x = 40, y = 210)

password_entry = Entry(frame,show = "*",font = ("yu gothic ui",13,"bold"),bg = "#00337C", fg = "white",width = 30)
password_entry.place(x = 45, y = 240)

                ################## Confirm Paswword label and enrty ##################

confirm_password_label = Label(frame, text = "Confirm Password", font = ("yu gothic ui",12,"bold"), bg = "#EEEEEE", fg = "#00337C")
confirm_password_label.place(x = 40, y = 275)

confirm_password_entry = Entry(frame,show = "*",font = ("yu gothic ui",13,"bold"),bg = "#00337C", fg = "white",width = 30)
confirm_password_entry.place(x = 45, y = 305)

                ################## Checkbutton I agree ##################

check = IntVar()
checkButton = Checkbutton(frame, variable = check,text = "I agree to the terms & Conditions", font = ("yu gothic ui",12,"bold"), bg = "#EEEEEE", fg = "#00337C")
checkButton.place(x = 40, y = 345)

                ################## Signup Button ##################

signup_button = Button(frame, text = "SIGNUP", font = ("yu gothic ui", 12, "bold"), fg = "White", bg = "#00337C", width = 29  , cursor="hand2", command = connect_database)
signup_button.place(x = 45, y = 400)


                ################## Show & Hide Button ##################

                
                
show_button = Image.open("D:\\SMI\\Images\\Show.png")
photo2 = ImageTk.PhotoImage(show_button)
show_button_label = Button(frame, image = photo2, bg = "#EEEEEE", activebackground = "#EEEEEE", cursor = "hand2", bd = 0, command = show)
show_button_label.image = photo2
show_button_label.place(x = 322, y = 240)
                
hide_button = Image.open("D:\\SMI\\Images\\hide.png")
photo1 = ImageTk.PhotoImage(hide_button)


window.mainloop()