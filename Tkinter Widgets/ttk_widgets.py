"""This file shows a sample Hello World program using Tkinter"""

from tkinter import *
from tkinter import ttk

# Main Window
root = Tk()
root.title("Hello World")
root.geometry("640x480")
root.minsize(320, 240)

# Style Config Ttk
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

# Frame Ttk
frm = ttk.Frame(root, padding=10)
frm.grid()

# Label Ttk
lbl = ttk.Label(frm, text="Hello World!", style="BW.TLabel")
lbl.grid(column=0, row=0)

# Label Ttk
btn = ttk.Button(frm, text="Quit", command=root.destroy)
btn.grid(column=1, row=0)

root.mainloop()
