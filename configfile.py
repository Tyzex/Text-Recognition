from text import *
from showtext import *
from tkinter import *
from PIL import Image, ImageTk


class Config(object):

    def __init__(self, root, filepath = None):
        self.root = root
        self.filepath = filepath
        self.root.after(1000, self.root.destroy())

    def newgui(self):
        if self.filepath is not None:
            new = Tk()
            new.title("Image-Text-Recognition")
            new.geometry("500x500")
            label = Label(new, text="Selected-Image")
            label.pack()
            img = Image.open(self.filepath)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            samplecanvas = Canvas(new, width=400, height=400)
            samplecanvas.pack()
            samplecanvas.create_image(300, 300, anchor=SE, image=img)

            txt = StringVar
            obj = ExtractText(self.filepath)
            txt = obj.gettext()
            obs = ShowText(new, txt)
            btn = Button(new, text="Extract Text", command=lambda: obs.showtext())
            btn.pack()
            mainloop()