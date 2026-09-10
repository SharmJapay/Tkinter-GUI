"""This file shows PanedWindow Widget of Tkinter"""

from tkinter import *

root = Tk()
root.title("PanedWindow Example")

paned_main = PanedWindow(root, orient=HORIZONTAL)
paned_main.pack(fill=BOTH, expand=1)

entry = Entry(paned_main, bd=5)
paned_main.add(entry)

# Create a PanedWindow widget
paned_vertical = PanedWindow(paned_main, orient=VERTICAL)
paned_main.add(paned_vertical)

scale = Scale(paned_vertical, orient=HORIZONTAL)
paned_vertical.add(scale)

root.mainloop()
