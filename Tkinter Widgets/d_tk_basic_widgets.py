"""This file shows Basic (Label, Button, Entry, CheckButton, RadioButton) Widgets of Tkinter"""

from tkinter import *


# Widget Functionalities
def change_text():
    """Changes text"""

    lbl_var.set(txtbox_var.get())
    change_btn.configure(state="disabled")
    reset_btn.configure(state="normal")


def reset():
    """Reset Default Values"""

    lbl_var.set("Default TkLabel")
    txtbox_var.set("")
    change_btn.configure(state="normal")
    reset_btn.configure(state="disabled")


def submit():
    """Submit Values"""

    print(f"Subscribe? {status_var.get()}")
    print(f"The gender is {gender_var.get()}")


# Initialize all Widgets
# Main root
root = Tk()
root.title("Tkinter Widgets")

# Initialize Variables
lbl_var = StringVar(value="Default TkLabel")
txtbox_var = StringVar(value="")
status_var = StringVar(value="No")
gender_var = StringVar(value="Male")

# To find out which are specific to a particular widget class:
for item in root.configure().keys():
    print(item)

# Create a Label widget
lbl = Label(root, textvariable=lbl_var, font=("Arial Bold", 20))
lbl.grid(column=1, row=0)

# Create a Entry widget
txtbox = Entry(root, width=15, textvariable=txtbox_var, font=("Arial Bold", 12))
txtbox.grid(column=1, row=1)

# Create a Button widget
change_btn = Button(
    root,
    width=15,
    text="Change Text",
    font=("Arial Bold", 10),
    command=change_text,
    state="normal",
)
change_btn.grid(column=0, row=3)

reset_btn = Button(
    root,
    width=15,
    text="Reset",
    font=("Arial Bold", 10),
    command=reset,
    state="disabled",
)
reset_btn.grid(column=2, row=3)

# Create a CheckButton widget
cb = Checkbutton(
    root, text="Subscribe", variable=status_var, onvalue="Yes", offvalue="No"
)
cb.grid(column=1, row=5)

# Create a RadioButton widget
radio1 = Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio1.grid(column=0, row=6)

radio2 = Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio2.grid(column=1, row=6)

radio3 = Radiobutton(root, text="Other", variable=gender_var, value="Other")
radio3.grid(column=2, row=6)

# Button trigger print of Checkbutton and Radiobutton
submit_btn = Button(
    root,
    width=15,
    text="Submit",
    font=("Arial Bold", 10),
    command=submit,
    state="normal",
)
submit_btn.grid(column=1, row=7)


# Run the Tkinter root
root.mainloop()
