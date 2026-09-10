"""This file shows How to center Tkinter App"""

import tkinter as tk

# Method 1:
root = tk.Tk()

width = 600  # Width
height = 300  # Height

screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

root.mainloop()

# Method 2:
root1 = tk.Tk()

label = tk.Label(root1, text="A Window")
label.place(x=70, y=80)

root1.eval("tk::PlaceWindow . center")
root1.mainloop()
