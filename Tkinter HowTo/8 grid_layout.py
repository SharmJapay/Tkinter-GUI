"""This file shows How to grid layout Tkinter app"""

# The grid layout has 4 main options that you can use while positioning widgets.

# * row – The row at which the widget is to be placed
# * column – The column at which the widget is to be placed
# * columnspan – The number of columns the widget will occupy
# *browspan – The number of rows the widget will occupy

import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

button1 = tk.Button(frame, text="Button 1")
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(frame, text="Button 2")
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(frame, text="Button 3")
button3.grid(row=1, column=0, padx=5, pady=5)

button4 = tk.Button(frame, text="Button 4")
button4.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()

# Example 2:

from tkinter import *

root1 = Tk()
root1.geometry("300x300")

for x in range(10):
    for y in range(7):
        entry = Entry(root1, width=6)
        entry.grid(row=x, column=y)

root1.mainloop()
