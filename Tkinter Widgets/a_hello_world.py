"""This file shows a sample Hello World program using Tkinter"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello World")
root.geometry("640x480")
root.minsize(320, 240)

frm = ttk.Frame(root, padding=10)
frm.grid()

# To find out the configuration options or methods on any widget:
print("\nForm")
print(frm.configure().keys())
print("\n")

lbl = ttk.Label(frm, text="Hello World!")
lbl.grid(column=0, row=0)

btn = ttk.Button(frm, text="Quit", command=root.destroy)
btn.grid(column=1, row=0)

# To find out which are specific to a particular widget class:
print("Label")
print(set(lbl.configure().keys()))
print("\n")
print("Button")
print(set(btn.configure().keys()))
print("\n")

# Similarly, you can find the available methods for a widget object using the standard dir() function
print(dir(btn))
print("\n")
print(set(dir(btn)) - set(dir(frm)))
print("\n")

root.mainloop()
