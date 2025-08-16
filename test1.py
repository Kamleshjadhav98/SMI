from time import time, sleep
from tkinter import *

def empty_textbox():
    textbox.delete("1.0", END)

root = Tk()

frame = Frame(root, width=300, height=100)
textbox = Text(frame)

frame.pack_propagate(0)
frame.pack()
textbox.pack()

textbox.insert(END, 'This is a test')
textbox.after(5000, empty_textbox)

root.mainloop()