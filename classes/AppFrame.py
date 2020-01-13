from tkinter import *
from .AnimatedLabel import AnimatedLabel
from .MouseMover import MouseMover

class AppFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        self.master = master
        self._gif_path = "shaking.gif"
        self._mouse_mover = MouseMover()
        self.pack(anchor="center", expand=1)
        self.create_widgets()
        self._mouse_mover.start()

    def toggle_shake(self):
        if self._animated_label.is_playing == True:
            self._animated_label.pause()
            self._mouse_mover.deactivate()
        else:
            self._animated_label.play()
            self._mouse_mover.activate()

        is_shaking = self._animated_label.is_playing
        self._toggle_btn["text"] = "Stop Shaking!" if is_shaking else "Shake!"
        self._toggle_btn["fg"] = "red" if is_shaking else "green"

    def quit(self):
        self._mouse_mover.join()
        self.master.destroy()

    def create_widgets(self):
        self._animated_label = AnimatedLabel(self, self._gif_path)

        # Buttons
        self._toggle_btn = Button(self, text="Shake!", fg="green", width=10)
        self._toggle_btn["command"] = self.toggle_shake
        self._toggle_btn.grid(pady=(0,10))

        self._quit_btn = Button(self, text="Quit", fg="white", bg="red", width=10)
        self._quit_btn["command"] = self.quit
        self._quit_btn.grid()