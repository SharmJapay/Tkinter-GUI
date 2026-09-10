"""This file shows Menu Widget of Tkinter"""

from tkinter import *

root = Tk()
root.title("Menu Example")
root.geometry("300x250")

# Create a Menu Widget
menu = Menu(root)
root.config(menu=menu)

# Create a Menu Item "File"
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Create a Menu Item "Help"
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

root.mainloop()
