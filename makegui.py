from getfile import *
from text import *
from showtext import *
from PIL import Image, ImageTk


class CreateGui(object):
    def __init__(self):
            filepath = "img.png"
            root = Tk()
            root.title("Image-Text-Recognition")
            root.geometry("500x500")
            label = Label(root, text="Sample-Image")
            label.pack()
            img = Image.open(filepath)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            samplecanvas = Canvas(root, width=400, height=400)
            samplecanvas.pack()
            samplecanvas.create_image(300, 300, anchor=SE, image=img)
            ob = GetFile(root)
            getbtn = Button(root, text="Browse Image", command=lambda: ob.getfilename())
            getbtn.pack()
            txt = StringVar
            obj = ExtractText(filepath)
            txt = obj.gettext()
            obs = ShowText(root, txt)
            btn = Button(root, text="Extract Text", command=lambda: obs.showtext())
            btn.pack()
            mainloop()