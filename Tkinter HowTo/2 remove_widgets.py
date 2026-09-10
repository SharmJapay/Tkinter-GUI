"""This file shows How to remove Tkinter app and widgets"""

# root.destroy()  # Destroys the whole Tkinter application
# mylabel.destroy()  # Destroys a label
# toplevel.destroy()  # Destroys a window

from tkinter import *


def close():
    """Closes the program"""
    root.destroy()


def delete():
    """Deletes the label widget"""
    mylabel.destroy()


root = Tk()
root.geometry("200x100")

button = Button(root, text="Close the window", command=close)
button.pack(pady=10)

root.mainloop()


# Example 2:
root1 = Tk()
root1.geometry("150x100")

mylabel = Label(root1, text="This is some random text")
mylabel.pack(pady=5)

mybutton = Button(root1, text="Delete", command=delete)
mybutton.pack(pady=5)

root1.mainloop()
