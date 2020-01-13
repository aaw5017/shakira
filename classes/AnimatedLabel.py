from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path

class AnimatedLabel(Label):
    def __init__(self, master, filename):
        gif_path = Path('./') / filename
        im = Image.open(gif_path)
        seq = []

        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))
        except EOFError:
            pass

        self.delay = 130
        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])
        temp = seq[0]

        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.is_playing = False
        self.idx = 0
        self.grid(row=1, sticky=W+E+N+S, padx=5, pady=5)

    def pause(self):
        self.master.after_cancel(self.cancel_token)
        self.is_playing = False

    def play(self):
        if self.is_playing == False:
            self.is_playing = True

        self.config(image=self.frames[self.idx])
        self.idx += 1
        if (self.idx == len(self.frames)):
            self.idx = 0
        self.cancel_token = self.master.after(self.delay, self.play)
