from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import csv
import pandas as pd

window = Toplevel()
window.geometry("1166x718")
window.title("View Attendance")
window.iconbitmap("D:\\SMI\\SMI1.ico")
window.state("zoomed")
window.resizable(0, 0)

window.config(bg = "white")

def callback(*args):
    n.get()
        

def callback2():
    sv2.get()

def callback3():
    sv3.get()

def set_combo_box():
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
    
    mycursor.execute("use employees")

    query = "select id from employee"
    mycursor.execute(query)

    rows = mycursor.fetchall()
    combo_box["values"] = rows

    scrollbar.configure(columns=("#1","#2","#3","#4","#5","#6"))
    
    scrollbar.heading("#0",text = "EID", anchor=W)
    scrollbar.heading("#1",text = "Name", anchor=W)
    scrollbar.heading("#2",text = "Year_Month", anchor=W)
    scrollbar.heading("#3",text = "Initial_Salary", anchor=W)
    scrollbar.heading("#4",text = "Commission", anchor=W)
    scrollbar.heading("#5",text = "Advance", anchor=W)
    scrollbar.heading("#6",text = "Final_Salary", anchor=W)

    scrollbar.column("#0",stretch=NO,minwidth=25,width=125)
    scrollbar.column("#1",stretch=NO,minwidth=0,width=200)
    scrollbar.column("#2",stretch=NO,minwidth=0,width=160)
    scrollbar.column("#3",stretch=NO,minwidth=0,width=160)
    scrollbar.column("#4",stretch=NO,minwidth=0,width=160)
    scrollbar.column("#5",stretch=NO,minwidth=0,width=160)
    scrollbar.column("#6",stretch=NO,minwidth=0,width=160)

def selectItem(a):
    selectItem.curItem = scrollbar.focus()
    selectItem.dictionary = scrollbar.item(selectItem.curItem)

def delete():       
    selectItem.curItem = scrollbar.focus()
    selectItem.dictionary = scrollbar.item(selectItem.curItem)
    res = selectItem.dictionary["values"]
    name = res[0]
    date = res[1]
    
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
    
    mycursor.execute("use final_salary_receipts")

    query = "delete from final_salary_receipt where name = %s and month_year = %s"
    mycursor.execute(query,(name,date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success","Record deleted successfully")

def search():
    n.get()
    month_year = f"{sv3.get()}-{sv2.get()}"
    try:
        conn = pymysql.connect(host = "localhost", user = "root", password = "pihu123")
        mycursor = conn.cursor()
    except:
        messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
    
    mycursor.execute("use final_salary_receipts")

    if sv2.get() != "" and sv3.get() != "":

        query = "select * from final_salary_receipt where id = %s and month_year = %s"
        mycursor.execute(query,(n.get(),month_year))
            
        row1 = mycursor.fetchall()

        for i in row1:
            scrollbar.insert(parent = "", index = "end",text = i[0],values = (i[1:]))

    
    
def print_receipt():
    cols = ['NAME','YEAR_MONTH','INITIAL_SALARY','COMMISSION','ADVANCE','FINAL_SALARY'] # Your column headings here
    path = 'D:\\SMI\\receipts\\salary.csv'
    excel_name = 'D:\\SMI\\receipts\\salary.xlsx'
    lst = []
    with open(path, "w", newline='') as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        for row_id in scrollbar.get_children():
            row = scrollbar.item(row_id,'values')
            lst.append(row)
        lst = list(map(list,lst))
        lst.insert(0,cols)
        csvwriter.writerow("")
        csvwriter.writerow("")
        csvwriter.writerow("")
        csvwriter.writerow("")
        csvwriter.writerow("\n")
        for row in lst:
            csvwriter.writerow(row)

    writer = pd.ExcelWriter(excel_name)
    df = pd.read_csv(path)
    df.to_excel(writer,'sheetname',index = False)
    writer.save()

def clear():
    for item in scrollbar.get_children():
      scrollbar.delete(item)
    
    month_entry.delete(0,END)
    year_entry.delete(0,END)
    combo_box.delete(0,END)

def back():
    window.update()
    window.iconify()
    

view_att_lbl = Label(window, text = "SALARY PRINT", font = ("yu gothic ui",50,"bold"),bg = "white",fg = "#00337C")
view_att_lbl.place(x = 470, y = 5)

id_label = Label(window, text = "Employee Id", font = ("yu gothic ui",23,"bold"), bg = "white", fg = "#00337C")
id_label.place(x = 10, y = 115)


n = StringVar()
combo_box = ttk.Combobox(window,width=70,textvariable=n)
combo_box.place(x = 14, y = 170)
n.trace("w",callback)


month_label = Label(window, text = "Month : ", font = ("yu gothic ui",22,"bold"), bg = "white", fg = "#00337C")
month_label.place(x = 475, y = 156) 

sv2 = StringVar()
month_entry = Entry(window,bg = "#00337C", fg = "white", width=10,font = ("yu gothic ui",13,"bold"), textvariable=sv2,validate="focusout",validatecommand=callback2)
month_entry.place(x = 600,y = 167)

year_label = Label(window, text = "Year : ", font = ("yu gothic ui",22,"bold"), bg = "white", fg = "#00337C")
year_label.place(x = 720, y = 156) 

sv3 = StringVar()
year_entry = Entry(window,bg = "#00337C", fg = "white", width=10,font = ("yu gothic ui",13,"bold"),textvariable=sv3,validate="focusout",validatecommand=callback3)
year_entry.place(x = 815,y = 167)

submit_button = Button(window, text = "SEARCH", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 10, cursor="hand2",command = search)
submit_button.place(x = 980, y = 157)

clear_button = Button(window, text = "CLEAR", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 10, cursor="hand2",command = clear)
clear_button.place(x = 1100, y = 157)

print_button = Button(window, text = "PRINT", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 10, cursor="hand2",command = print_receipt)
print_button.place(x = 1220, y = 157)

delete_button = Button(window, text = "DELETE", font = ("yu gothic ui", 12, "bold"), fg = "white", bg = "#00337C", width = 10, cursor="hand2",command = delete)
delete_button.place(x = 1220, y = 107)

back_button = Button(window, text = "<-", font = ("yu gothic ui", 27, "bold"), fg = "#00337C", bg = "white", width = 2, cursor="hand2",command = back, bd = 0)
back_button.place(x = 20, y = 0)

scrollbarx = Scrollbar(window, orient=HORIZONTAL)
scrollbary = Scrollbar(window, orient=VERTICAL)

scrollbar = ttk.Treeview(window)
scrollbar.place(relx=0.01,rely=0.318,width=1287,height=450)
scrollbar.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
scrollbar.configure(selectmode="extended")
scrollbar.bind('<ButtonRelease-1>', selectItem)

scrollbary.configure(command=scrollbar.yview)
scrollbarx.configure(command=scrollbar.xview)

scrollbarx.place(relx=0.009,rely=0.922,width=1300,height=22)
scrollbary.place(relx=0.953,rely = 0.319,width=22,height=450)
set_combo_box()

