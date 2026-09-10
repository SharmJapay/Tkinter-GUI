"""This file shows Scale Widget of Tkinter"""

from tkinter import *

root = Tk()

# Create a Vertical scale
vertical_scale = Scale(root, from_=0, to=42)
vertical_scale.pack()

# Create a Horizontal scale
horizontal_scale = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal_scale.pack()

root.mainloop()
