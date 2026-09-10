"""This file shows Canvas Widget of Tkinter"""

from tkinter import *

root = Tk()
root.title("Canvas Example")

# Create a Canvas widget
canvas = Canvas(root, width=200, height=60)
canvas.pack()

y = 30
canvas.create_line(0, y, 200, y)
root.mainloop()
