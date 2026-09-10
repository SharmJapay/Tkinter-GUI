"""This file shows Combobox Widget of Tkinter"""

import tkinter as tk
from tkinter import ttk


def select(event):
    """Returns combobox selected value"""

    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)


root = tk.Tk()
root.title("Combobox Example")

label = tk.Label(root, text="Selected Item:")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(
    root, values=["Option 1", "Option 2", "Option 3"], state="readonly"
)
combo_box.pack(pady=5)

combo_box.set("Option 1")
combo_box.bind("<<ComboboxSelected>>", select)

root.mainloop()
