"""This file shows Menubutton Widget of Tkinter"""

from tkinter import *

root = Tk()

# Create a Menubutton widget
mb = Menubutton(root, text="GfG")
mb.grid()

mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

contact_var = IntVar()
about_var = IntVar()

mb.menu.add_checkbutton(label="Contact", variable=contact_var)
mb.menu.add_checkbutton(label="About", variable=about_var)
mb.pack()

root.mainloop()
