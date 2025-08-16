# from datetime import datetime

# d1 = datetime.strptime("24 January 2023 01:15 PM", "%d %B %Y %I:%M %p")
# d2 = datetime.strptime("24 January 2023 10:00 PM", "%d %B %Y %I:%M %p")

# print(d2 - d1)

# from tkinter import *

# def callback(sv):
#     print(sv.get())

# root = Tk()
# sv = StringVar()
# sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
# e = Entry(root, textvariable=sv)
# e.pack()
# root.mainloop()  
# s = "5:21:00"
# print(s[0:2])

# from datetime import datetime

# timestr = "12/13/2020 7:59"
    
# dt = datetime.strptime(timestr, '%m/%d/%Y %H:%M')
# corrected = datetime.strftime(dt, '%m/%d/%Y %H:%M')
    
# print(corrected)

# hours, minutes = map(int, "11:15".split(':'))
# print(hours)
# print(minutes)

# print(15 / 60)

# from datetime import datetime

# form = "%d %B %Y %I:%M %p"
# d1 = datetime.strptime("26 January 2023 12:05 PM",form)
# d2 = datetime.strptime("26 January 2023 08:05 PM",form)
# diff = str(d2 - d1)
# print(diff)

str1 = "2023-01"

year, month = map(int,str1.split("-"))
print(year)
print(month)