from tkinter import *
from tkinter.ttk import Progressbar

window_loading = Tk()
window_loading.resizable(0,0)
window_loading.config(background = "white")

width = 530
height = 430

x = (window_loading.winfo_screenwidth()//2) - (width // 2)
y = (window_loading.winfo_screenheight()//2) - (height // 2)

window_loading.geometry("{}x{}+{}+{}".format(width,height,x,y))
window_loading.wm_attributes("-topmost", True)
window_loading.overrideredirect(1)


i = 0

def load():
    global i
    if i <= 10:
        txt = "Please wait..." + str(10 * i) + "%"
        progress_lbl.config(text = txt)
        progress_lbl.after(500, load)
        progressbar["value"] = 10*i
        i = i + 1
    else:
        window_loading.destroy()
        import login



image = PhotoImage(file = "D:\SMI\Images\SMI.png")
image_lbl = Label(window_loading, image = image, bg = "white")
image_lbl.place(x = 155, y = 30)

name_lbl = Label(window_loading, text = "SHRI MAHESHWARI INDUSTRIES" , font = ("yu gothic ui", 21 , "bold"), fg = "#000B49", bg = "white")
name_lbl.place(x = 60, y = 290)

progress_lbl = Label(window_loading , text = "Please wait..." , font = ("yu gothic ui" , 13 , "bold") , bg = "white")
progress_lbl.place(x = 205, y = 330)

progressbar = Progressbar(window_loading, orient=HORIZONTAL, length = 500, mode = "determinate")
progressbar.place(x = 15, y = 370)

load()

window_loading.mainloop()