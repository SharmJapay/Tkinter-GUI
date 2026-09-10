"""This file shows Message Widget of Tkinter"""

from tkinter import *

root = Tk()

MESSAGE_TEXT = "This is our Message"

# Create a Message widget
message = Message(root, text=MESSAGE_TEXT)
message.config(bg="lightgreen")
message.pack()

root.mainloop()
