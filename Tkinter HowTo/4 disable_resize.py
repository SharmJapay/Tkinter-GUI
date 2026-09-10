"""This file shows How to disable resize Tkinter app"""

import tkinter as tk

root = tk.Tk()
root.geometry("200x150")

label = tk.Label(root, text="Hello World")
label.pack(padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
