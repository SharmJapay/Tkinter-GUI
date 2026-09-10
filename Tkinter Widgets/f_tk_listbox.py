"""This file shows Listbox Widget of Tkinter"""

from tkinter import *


def get_selected():
    """Returns listbox selected values"""

    # 1. Get a tuple of selected index numbers (e.g., (1,))
    selected_indices = listbox.curselection()

    # 2. Check if the user actually selected something
    if selected_indices:
        # Loop through indices (works for both single and multiple selection)
        for index in selected_indices:
            value = listbox.get(index)
            print(f"Selected value: {value}")
    else:
        print("No item selected.")


root = Tk()
root.title("Listbox Example")
root.geometry("300x250")

# Create a Listbox widget and insert items
listbox = Listbox(root, selectmode=SINGLE)  # or MULTIPLE
listbox.pack(pady=10)

for item in ["Python", "Java", "C++", "JavaScript"]:
    listbox.insert(END, item)

# Button to trigger the value retrieval
btn = Button(root, text="Get Selection", command=get_selected)
btn.pack(pady=10)

root.mainloop()
