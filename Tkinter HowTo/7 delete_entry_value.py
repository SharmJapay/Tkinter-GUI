"""This file shows How to delete entry value Tkinter app"""

from tkinter import *


def delete():
    """Delete entry value"""
    myentry.delete(3, "end")


root = Tk()
root.geometry("180x120")

myentry = Entry(root, width=20)
myentry.pack(pady=5)

mybutton = Button(root, text="Delete", command=delete)
mybutton.pack(pady=5)

root.mainloop()
