"""This file shows Text Widget of Tkinter"""

from tkinter import *

root = Tk()
root.title("Text Widget Example")

# Create a Text widget
text_widget = Text(root, height=2, width=30)
text_widget.pack()

text_widget.insert(END, "GeeksforGeeks\nBEST WEBSITE\n")
root.mainloop()
