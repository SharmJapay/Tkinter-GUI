"""This file shows How to close Tkinter App"""

from tkinter import *


def close():
    """Closes the program"""
    root.destroy()


root = Tk()
root.geometry("200x100")

button = Button(root, text="Close the window", command=close)
button.pack(pady=10)

root.mainloop()

# Optimize version
root1 = Tk()
root1.geometry("200x100")

button = Button(root1, text="Close the window", command=root1.destroy)
button.pack(pady=10)

root1.mainloop()
