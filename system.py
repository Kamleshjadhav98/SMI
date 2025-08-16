from tkinter import *
from PIL import Image, ImageTk
import sys

window = Tk()
window.title("PAYROLL SYSTEM")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.state("zoomed")
window.resizable(0,0)
window.config(bg = "white")

def complete_profile():
    from addEmployee import window_employee
    window_employee.deiconify()

def view_profile():
    from viewEmployee import window_view_employee
    window_view_employee.deiconify()

def update_profile():
    from update import window_employee
    window_employee.deiconify()

def in_time():
    from inAttendance import window
    window.update()
    window.deiconify()

def out_time():
    from outAttendance import window
    window.update()
    window.deiconify()

def view_attendance():
    from viewAttendance import window
    window.deiconify()

def over_time():
    from overtime import window
    window.deiconify()

def advance_emp():
    from advance import window
    window.deiconify()

def view_advance():
    from viewAdvance import window
    window.deiconify()

def emp_sal():
    from totalSalary import window
    window.deiconify()

def sal_details():
    from salary import window
    window.deiconify()

def delete_employee():
    from deleteEmployee import window
    window.deiconify()

def logout():
    sys.exit()

bg_frame = Image.open("D:\\SMI\\Images\\SMI2.png")
bg_photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(window, image = bg_photo, bg = "white")
bg_panel.image = bg_photo
bg_panel.place(x = 500, y = 90)

smi_name = Label(window, text = "SHRI MAHESHWARI INDUSTRIES", bg = "white", fg = "#000B49", font = ("yu gothic ui",28,"bold"))
smi_name.place(x = 397, y = 570)

smi_sub_name = Label(window, text = "PAYROLL SYSTEM", bg = "white", fg = "#000B49", font = ("yu gothic ui",25,"bold"))
smi_sub_name.place(x = 540, y = 620)

menubar = Menu()

employee = Menu(menubar, tearoff=False)
update = Menu(menubar, tearoff=False)
attendance = Menu(menubar, tearoff=False)
overtime = Menu(menubar, tearoff = False)
advance = Menu(menubar, tearoff=False)
salary = Menu(menubar, tearoff=False)
delete = Menu(menubar, tearoff=False)
exit = Menu(menubar, tearoff=False)

employee.add_command(label="Add New Employee",command = complete_profile)
employee.add_command(label="View Profile",command = view_profile)

update.add_command(label = "Update Employee",command = update_profile)

attendance.add_command(label = "In Time", command = in_time)
attendance.add_command(label = "Out Time", command = out_time)
attendance.add_command(label = "View Attendance", command = view_attendance)

overtime.add_command(label = "Add Overtime", command = over_time)

advance.add_command(label = "Give Advance", command = advance_emp)
advance.add_command(label = "View Advance",command = view_advance)


salary.add_command(label = "Calculate Salary",command = emp_sal)
salary.add_command(label = "View Salary Details",command = sal_details)

delete.add_command(label = "Delete Employee",command = delete_employee)

exit.add_command(label = "Logout",command=logout)

menubar.add_cascade(label="Employee", menu=employee)
menubar.add_cascade(label="Update", menu=update)
menubar.add_cascade(label="Attendance", menu=attendance)
menubar.add_cascade(label = "OverTime",menu = overtime)
menubar.add_cascade(label = "Advance", menu = advance)
menubar.add_cascade(label="Salary", menu=salary)
menubar.add_cascade(label="Delete", menu=delete)
menubar.add_cascade(label="Exit", menu=exit)

window.config(menu=menubar)



window.mainloop()