#!/usr/bin/env python3

from tkinter import *
from classes.AnimatedLabel import AnimatedLabel
from classes.MouseMover import MouseMover

def toggle_shake(anim: AnimatedLabel, mm: MouseMover, btn: Button):
    if anim_label.is_playing == True:
        anim_label.pause()
        mm.deactivate()
    else:
        anim_label.play()
        mm.activate()

    is_shaking = anim_label.is_playing
    btn["text"] = "Stop Shaking!" if is_shaking else "Shake!"
    btn["fg"] = "red" if is_shaking else "green"

def quit(master, mover: MouseMover):
    mover.join()
    master.destroy()

# Master Window
master = Tk()
master_width = 600
master_height= 300
x_coord = int(master.winfo_screenwidth()/2 - master_width/2)
y_coord = int(master.winfo_screenheight()/2 - master_height/2)
master.geometry("%dx%d+%d+%d" % (master_width, master_height, x_coord, y_coord))
master.title("Shakira App")

# Body
body_frame = Frame(master)
body_frame.pack(side="top", anchor="center", expand=1)

# Class objects
anim_label = AnimatedLabel(body_frame, "shaking.gif")
mm = MouseMover()

# Buttons
toggle_btn = Button(body_frame, text="Shake!", fg="green", command=lambda: toggle_shake(anim_label, mm, toggle_btn), width=10)
toggle_btn.grid()
quit_btn = Button(body_frame, text="Quit", fg="red", command=lambda: quit(master, mm), width=10)
quit_btn.grid()

# start the app
master.protocol("WM_DELETE_WINDOW", lambda: quit(master, mm))
mm.start()
master.mainloop()