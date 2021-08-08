from tkinter import *

class ShowText(object):

    def __init__(self, root = None, txt = None):
        self.root = root
        self.txt = txt

    def showtext(self):
        if self.txt is not None:
            #self.txt = StringVar()
            #self.txt.set(txt)
            new = Toplevel(self.root)
            new.title("Extracted Text")
            new.geometry("300x300")
            label = Label(new, text=self.txt)
            # label = Entry(new, bd=0, state="readonly")
            # label.configure(textvariable=txt)
            # label.place(height=200, width=200)
            # label.insert(new, self.text)
            label.pack()
        else:
            self.root.title("Something Went Wrong")
            self.root.geometry("200x200")
            self.root.after(5000, lambda e: self.root.destroy())
