"""This file shows how to use variables in Tkinter"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create the application variable and give it an initial value.
contents = tk.StringVar(value="this is a variable")

# Tell the entry widget to track the variable.
entry = ttk.Entry(root, textvariable=contents)
entry.pack()


# Print the current value whenever the user presses Return or [Enter] Key.
def print_contents(event):
    print(f"\nEvent: {event}")
    print("\nThe current entry content is:", contents.get())


entry.bind("<Return>", print_contents)


# Setting the variable from the program updates the entry through the
# same link.
def clear():
    contents.set("")


ttk.Button(root, text="Clear", command=clear).pack()


root.mainloop()
