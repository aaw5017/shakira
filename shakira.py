#!/usr/bin/env python3

from tkinter import *
from classes.AppFrame import AppFrame

# Master Window
master = Tk()
master_width = 600
master_height= 300
x_coord = int(master.winfo_screenwidth()/2 - master_width/2)
y_coord = int(master.winfo_screenheight()/2 - master_height/2)
master.geometry("%dx%d+%d+%d" % (master_width, master_height, x_coord, y_coord))
master.title("Shakira App")

# Start Shakira
app = AppFrame(master=master)
master.protocol("WM_DELETE_WINDOW", app.quit)
master.mainloop()