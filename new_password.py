from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox


window = Tk()
window.title("CHANGE PASSWORD")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.geometry("116x718")
window.state("zoomed")
window.resizable(0,0)

bg_frame = Image.open("D:\\SMI\\Images\\background1.png")
bg_photo = ImageTk.PhotoImage(bg_frame)
bg_photo_label = Label(window, image = bg_photo)
bg_photo_label.image = bg_photo
bg_photo_label.pack(fill = "both", expand = "yes")

def show():
        hide_button_label = Button(frame, image = photo1, bg = "white", activebackground = "white", cursor = "hand2", bd = 0,command = hide)
        hide_button_label.image = photo1
        hide_button_label.place(x = 455, y = 340)
        password_entry.config(show = '')
        confirm_password_entry.config(show = '')
                
def hide():
        show_button_label = Button(frame, image = photo2, bg = "white", activebackground = "white", cursor = "hand2", bd = 0, command = show)
        show_button_label.image = photo2
        show_button_label.place(x = 455, y = 340)
        password_entry.config(show = "*")
        confirm_password_entry.config(show = "*")



def validate():
      try:           
         conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
         mycursor = conn.cursor()

      except:
         messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        
        
      
      mycursor.execute("use employeedata")
        
      query = "select * from employee where username = %s"
      mycursor.execute(query,(username_entry.get()))

      row = mycursor.fetchone()
      validate.value = row
      if username_entry.get() == "":
         messagebox.showerror("Error", "First enter a registered username")
      elif validate.value == None:
         messagebox.showerror("Error","Username does not exist")
      else:
         messagebox.showinfo("Success","Now you can create a new password")
        
def update():

      if username_entry.get() == "":
         messagebox.showerror("Error", "First enter a registered username and validate it")
      elif password_entry.get() == "" and confirm_password_entry.get() == "":
         messagebox.showerror("Error", "All fields are required")    
      elif password_entry.get() != confirm_password_entry.get():
         messagebox.showerror("Error","Password Mismatched")
      elif validate.value == None:
         messagebox.showerror("Error", "Username does not exists")
      elif validate.value != None:
         try:           
            conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
            mycursor = conn.cursor()

         except:
            messagebox.showerror("Error","Database Connectivity Issue, Try Again")
        
         try:
            query = "create database employeedata"
            mycursor.execute(query)
            query = "use employeedata"
            mycursor.execute(query)
            query = "create table employee(id int primary key not null, email varchar(50), username varchar(100), password varchar(20))"
            mycursor.execute(query)
        
         except:
            mycursor.execute("use employeedata")
                
         query = "update employee set password = %s where username = %s"
         mycursor.execute(query,(password_entry.get(),username_entry.get()))
         conn.commit()
         conn.close()
         messagebox.showinfo("Success","Password changed successfully!!!")
         window.destroy()
         import login
                    

frame = Frame(window, width = 550, height = 600, bg = "white")
frame.place(x = 420, y = 90)

heading_Label = Label(frame, text = "CHANGE PASSWORD", bg = "white", fg = "#00337C", font = ("yu gothic ui",35,"bold"))
heading_Label.place(x = 50, y = 15)

username_label = Label(frame, text = "Enter registered username", font = ("yu gothic ui",16,"bold"), bg = "white", fg = "#00337C")
username_label.place(x = 80, y = 110)

username_entry = Entry(frame,font = ("yu gothic ui",13,"bold"),bg = "#00337C", fg = "white",width = 40)
username_entry.place(x = 85, y = 160)

validate_button = Button(frame, text = "VALIDATE", font = ("yu gothic ui", 12, "bold"), fg = "White", bg = "#00337C", width = 20, cursor="hand2", command = validate)
validate_button.place(x = 175, y = 220)

password_label = Label(frame, text = "New Password", font = ("yu gothic ui",15,"bold"), bg = "white", fg = "#00337C")
password_label.place(x = 80, y = 290)

password_entry = Entry(frame, show = "*", font = ("yu gothic ui",13,"bold"),bg = "#00337C", fg = "white",width = 40)
password_entry.place(x = 85, y = 340)

confirm_password_label = Label(frame, text = "Confirm Password", font = ("yu gothic ui",15,"bold"), bg = "white", fg = "#00337C")
confirm_password_label.place(x = 80, y = 380)

confirm_password_entry = Entry(frame, show = "*", font = ("yu gothic ui",13,"bold"),bg = "#00337C", fg = "white",width = 40)
confirm_password_entry.place(x = 85, y = 430)


show_button = Image.open("D:\\SMI\\Images\\Show.png")
photo2 = ImageTk.PhotoImage(show_button)
show_button_label = Button(frame, image = photo2, bg = "white", activebackground = "white", cursor = "hand2", bd = 0, command = show)
show_button_label.image = photo2
show_button_label.place(x = 455, y = 340)
                
hide_button = Image.open("D:\\SMI\\Images\\hide.png")
photo1 = ImageTk.PhotoImage(hide_button)

update_button = Button(frame, text = "UPDATE", font = ("yu gothic ui", 12, "bold"), fg = "White", bg = "#00337C", width = 20, cursor="hand2",command = update)
update_button.place(x = 175, y = 500)


window.mainloop()