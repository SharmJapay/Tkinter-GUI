"""This file shows How to change font Tkinter app"""

# Technique 1:
# from tkinter import Tk, font

# root = Tk()
# print(font.families())

import tkinter as tk

root = tk.Tk()
root.option_add("*Font", "Times 19")
root.geometry("200x150")

label = tk.Label(root, text="Hello World")
label.pack(padx=5, pady=5)

root.mainloop()


# Technique 2:
# import tkinter as tk
# import tkinter.font as tkFont

# root = tk.Tk()
# print(tkFont.names())


import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("200x150")

def_font = tk.font.nametofont("TkDefaultFont")
def_font.config(size=24)

label = tk.Label(root, text="Hello World")
label.pack(padx=5, pady=5)

root.mainloop()
