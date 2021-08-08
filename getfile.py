from tkinter import filedialog
from configfile import *

class GetFile(object):
    def __init__(self, root):
        self.root = root
        self.filename = None

    def getfilename(self):
        self.filepath = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                                   filetypes=(("Image Files", "*.png*"),
                                                              ("All Files", "*.*")))
        if self.filepath is not None:
            obj = Config(self.root, self.filepath)
            obj.newgui()

    def getfilepath(self):
        return self.filepath