"""This file shows Spinbox Widget of Tkinter"""

from tkinter import *

root = Tk()
root.title("Spinbox Example")

# Create a Spinbox widget
spinbox = Spinbox(root, from_=0, to=10)
spinbox.pack()

root.mainloop()
