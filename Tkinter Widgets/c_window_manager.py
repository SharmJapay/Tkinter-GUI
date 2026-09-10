"""This file shows how to create a window using Tkinter module"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Tutorial")
root.geometry("640x480")
root.minsize(320, 240)

# To find out which are specific to a particular widget class:
for item in root.configure().keys():
    print(item)

print("\n")

# Similarly, you can find the available methods for a widget object using the standard dir() function
for item in dir(root):
    print(item)

ttk.Label(root, text="Hello").pack(padx=20, pady=20)

root.mainloop()
