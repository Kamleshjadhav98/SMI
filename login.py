from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
        
window = Tk()
window.title("LOGIN")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.geometry("1166x178")
window.state("zoomed")
window.resizable(0, 0)

bg_frame = Image.open("D:\\SMI\\Images\\background1.png")
bg_photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window, image = bg_photo)
bg_panel.image = bg_photo
bg_panel.pack(fill = "both", expand = "yes")

def on_enter_username(event):
        if username_entry.get() == "Username":
                username_entry.delete(0,END)

def on_enter_password(event):
        if password_entry.get() == "Password":
                password_entry.delete(0,END)
                password_entry.config(show = "*")

def show():
        hide_button_label = Button(frame, image = photo1, bg = "#EEEEEE", activebackground = "#EEEEEE", cursor = "hand2", bd = 0,command = hide)
        hide_button_label.image = photo1
        hide_button_label.place(x = 258, y = 193)
        password_entry.config(show = '')
def hide():
        show_button_label = Button(frame, image = photo2, bg = "#EEEEEE", activebackground = "#EEEEEE", cursor = "hand2", bd = 0, command = show)
        show_button_label.image = photo2
        show_button_label.place(x = 258, y = 193)
        password_entry.config(show = "*")

def forgot_password():
        window.destroy()
        import otp

def create():
        window.destroy()
        import signup

def login_user():
        if username_entry.get() == "" or password_entry.get() == "":
                messagebox.showerror("Error", "All Fields are Required")

        else:
                try:
                        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
                        mycursor = conn.cursor()
                
                except:
                        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
                        return

                query = "use employeedata"
                mycursor.execute(query)
                query = "select * from employee where username = %s and password = %s"
                mycursor.execute(query,(username_entry.get(),password_entry.get()))
                row = mycursor.fetchone()

                if row == None:
                        messagebox.showerror("Error", "Invalid username or password")

                else:
                        window.destroy()
                        import system                
                ################## Main Frame ##################

lg_frame = Frame(window, width=900, height = 600, bg = "white")
lg_frame.place(x = 200, y = 70)

                ################## Welcome Heading ##################

heading = Label(lg_frame, text = "WELCOME", font = ("yu gothic ui", 25, "bold"), bg = "white", fg = "#00337C")
heading.place(x = 70, y = 30, width = 300, height = 30)

                ################## SMI image ##################

side_left = Image.open("D:\\SMI\\Images\\SMI1.png")
photo = ImageTk.PhotoImage(side_left)
side_image_label = Label(lg_frame, image = photo, bg = "white")
side_image_label.image = photo
side_image_label.place(x = 70, y = 100)

                ################## SMI name label ##################

name_lbl = Label(lg_frame, text = "SHRI MAHESHWARI INDUSTRIES" , font = ("yu gothic ui", 17 , "bold"), fg = "#000B49", bg = "white")
name_lbl.place(x = 50, y = 520)

                ################## Details Frame ##################

frame = Frame(lg_frame, width = 350, height = 500, bg = "#EEEEEE")
frame.place(x = 510, y = 50)

################## User Login label ##################

userLogin = Label(frame , text = "USER LOGIN" , font = ("yu gothic ui" , 20, "bold"), bg = "#EEEEEE", fg = "#00337C")
userLogin.place(x = 90, y = 30)

                ################## Username entry ##################

username_entry = Entry(frame, width = 25, font = ("yu gothic ui", 12, "bold"), bd = 0, fg = "#00337C", bg = "#EEEEEE" )
username_entry.place(x = 30, y = 130)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", on_enter_username)

username_line = Canvas(frame, highlightthickness=0, width=255, height = 2.0, bg = "#00337C")
username_line.place(x = 30, y = 155)

                ################## Password label, entry ##################

password_entry = Entry(frame,width = 25, font = ("yu gothic ui", 12, "bold"), bd = 0, fg = "#00337C", bg = "#EEEEEE" )
password_entry.insert(0, "Password")
password_entry.place(x = 30, y = 195)
password_entry.bind("<FocusIn>", on_enter_password)

password_line = Canvas(frame, highlightthickness=0, width=255, height = 2.0, bg = "#00337C")
password_line.place(x = 30, y = 220)

                ################## Show & Hide Button ##################


show_button = Image.open("D:\\SMI\\Images\\Show.png")
photo2 = ImageTk.PhotoImage(show_button)
show_button_label = Button(frame, image = photo2, bg = "#EEEEEE", activebackground = "#EEEEEE", cursor = "hand2", bd = 0, command = show)
show_button_label.image = photo2
show_button_label.place(x = 258, y = 193)

hide_button = Image.open("D:\\SMI\\Images\\hide.png")
photo1 = ImageTk.PhotoImage(hide_button)





                ################## Forgot Button ##################

forgot_btn = Button(frame, text = "Forgot Password ?",bg = "#EEEEEE", fg = "black", activebackground = "#EEEEEE", font = ("yu gothic ui" , 11, "bold underline"), cursor = "hand2", bd = 0, command = forgot_password)
forgot_btn.place(x = 152, y = 230)

                ################## Login Button ##################


login_button = Button(frame, text = "LOGIN", font = ("yu gothic ui", 12, "bold"), fg = "White", bg = "#00337C", width = 27, cursor="hand2", command = login_user)
login_button.place(x = 35, y = 295)

                ################## Signup label & Button ##################
signup_lbl = Label(frame, text = "No account yet?", bg = "#EEEEEE", fg = "black", font = ("yu gothic ui",12,"bold"))
signup_lbl.place(x = 35, y = 345)

signup_button = Button(frame, text = "Create new one", font = ("yu gothic ui", 11, "bold underline"), fg = "#00337C", bg = "#EEEEEE",bd = 0, cursor = "hand2", command = create)
signup_button.place(x = 180, y = 342)

                ################## Follow Us label ##################

follow_us_label = Label(frame, text = "Follow us on", font = ("yu gothic ui",13,"bold"), bg = "#EEEEEE", fg = "black")
follow_us_label.place(x = 120, y = 390)


                ################## Social media Images ##################

fb_button = Image.open("D:\\SMI\\Images\\facebook.png")
photo3 = ImageTk.PhotoImage(fb_button)
fb_button_label = Button(frame, image = photo3, bg = "#EEEEEE", bd = 0, cursor = "hand2")
fb_button_label.image = photo3
fb_button_label.place(x = 70, y = 430)

insta_button = Image.open("D:\\SMI\\Images\\instagram.png")
photo4 = ImageTk.PhotoImage(insta_button)
insta_button_label = Button(frame, image = photo4, bg = "#EEEEEE", bd = 0, cursor = "hand2")
insta_button_label.image = photo4
insta_button_label.place(x = 140, y = 430)

twitter_button = Image.open("D:\\SMI\\Images\\twitter.png")
photo5 = ImageTk.PhotoImage(twitter_button)
twitter_button_label = Button(frame, image = photo5, bg = "#EEEEEE", bd = 0, cursor = "hand2")
twitter_button_label.image = photo5
twitter_button_label.place(x = 210, y = 430)





window.mainloop()
