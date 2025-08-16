from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
import smtplib
import ssl
import pymysql

smtp_port = 587
smtp_server = "smtp.gmail.com"


window = Tk()
window.title("OTP VERIFICATION")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.geometry("1166x178")
window.state("zoomed")
window.resizable(0, 0)

bg_frame = Image.open("D:\\SMI\\Images\\background1.png")
bg_photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window, image = bg_photo)
bg_panel.image = bg_photo
bg_panel.pack(fill = "both", expand = "yes")


def submit_email():
        
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
        mycursor = conn.cursor()

    except:
        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
        return


    mycursor.execute("use employeedata")
        
    query = "select * from employee where email = %s"
    mycursor.execute(query,(email_entry.get()))

    row = mycursor.fetchone()

    if row == None:
        messagebox.showerror("Error", "Not a registered email")

    else:    
        email = email_entry.get()
        email_from = email
        email_to = email
        pswd = "cqzmpnginwzypidi"
        n = str(random.randint(1000,9999))
        submit_email.otp = n
        simple_email_context = ssl.create_default_context()

        try:
            TIE_server = smtplib.SMTP(smtp_server,smtp_port)
            TIE_server.starttls(context=simple_email_context)
            TIE_server.login(email_from,pswd)
            TIE_server.sendmail(email_from,email_to,submit_email.otp)

        except:
            pass

        finally:
            conn.close()
            TIE_server.quit()

def resend_btn():
    
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
        mycursor = conn.cursor()

    except:
        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
        return

    
    mycursor.execute("use employeedata")
        
    query = "select * from employee where email = %s"
    mycursor.execute(query,(email_entry.get()))

    row = mycursor.fetchone()

    if row == None:
        messagebox.showerror("Error", "Not a registered email")

    else:    

        email = email_entry.get()
        email_from = email
        email_to = email
        pswd = "bsflqndedelmwukz"
        n = str(random.randint(1000,9999))
        submit_email.otp = n
        simple_email_context = ssl.create_default_context()

        try:
            TIE_server = smtplib.SMTP(smtp_server,smtp_port)
            TIE_server.starttls(context=simple_email_context)
            TIE_server.login(email_from,pswd)
            TIE_server.sendmail(email_from,email_to,submit_email.otp)

        except:
            pass

        finally:
            conn.close()
            TIE_server.quit()

      

def check_otp():
    try:
        userInput = otp_entry.get()
        if userInput == submit_email.otp:
            window.destroy()
            import new_password
            

        elif userInput != submit_email.otp or userInput != resend_btn.otp:
            messagebox.showerror("Error", "Wrong OTP")
   
    except:
        messagebox.showerror("Error", "INVALID OTP")        


otp_frame = Frame(window, width=550, height=600, bg = "white")
otp_frame.place(x = 420, y = 90)


heading_Label = Label(otp_frame, text = "OTP VERIFICATION", bg = "white", fg = "#00337C", font = ("yu gothic ui",30,"bold"))
heading_Label.place(x = 100, y = 15)

email_label = Label(otp_frame, text = "Enter registered email", bg = "white", fg = "#00337C", font = ("yu gothic ui",18,"bold"))
email_label.place(x = 80, y = 100)

email_entry = Entry(otp_frame,width = 25, font = ("yu gothic ui", 12, "bold"), bd = 0, fg = "#00337C", bg = "white" )
email_entry.place(x = 85, y = 160)

email_line = Canvas(otp_frame, highlightthickness=0, width=350, height = 2.0, bg = "#00337C")
email_line.place(x = 85, y = 185)

submit_otp_button = Button(otp_frame, text = "SUBMIT", font = ("yu gothic ui", 12, "bold"), fg = "White", bg = "#00337C", width = 20, cursor="hand2", command = submit_email)
submit_otp_button.place(x = 165, y = 235)

otp_label = Label(otp_frame, text = "Enter OTP", bg = "white", fg = "#00337C", font = ("yu gothic ui",18,"bold"))
otp_label.place(x = 80, y = 315)

otp_entry = Entry(otp_frame,width = 25, font = ("yu gothic ui", 12, "bold"), bd = 0, fg = "#00337C", bg = "white" )
otp_entry.place(x = 85, y = 365)

otp_line = Canvas(otp_frame, highlightthickness=0, width=350, height = 2.0, bg = "#00337C")
otp_line.place(x = 85, y = 390)

verify_otp_button = Button(otp_frame, text = "VERIFY OTP", font = ("yu gothic ui", 12, "bold"), fg = "White", bg = "#00337C", width = 20, cursor="hand2", command = check_otp)
verify_otp_button.place(x = 165, y = 445)

resend_otp_button = Button(otp_frame, text = "RESEND OTP", font = ("yu gothic ui", 12, "bold"), fg = "White", bg = "#00337C", width = 20, cursor="hand2", command = resend_btn)
resend_otp_button.place(x = 165, y = 510)

window.mainloop()
