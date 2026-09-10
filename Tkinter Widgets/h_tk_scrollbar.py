"""This file shows Scrollbar Widget of Tkinter"""

from tkinter import *


def print_scrollbar_position():
    """Returns the position of scrollbar"""

    # .get() returns a tuple like (0.25, 0.75)
    low, high = scrollbar.get()
    print(f"Scrollbar starts at: {low:.2f} ({low * 100:.0f}%)")
    print(f"Scrollbar ends at: {high:.2f} ({high * 100:.0f}%)")
    print("-" * 30)


root = Tk()
root.title("Scrollbar Value Example")
root.geometry("400x300")

# Create a Frame to hold the Text widget and its Scrollbar widget together
text_frame = Frame(root)
text_frame.pack(side=TOP, fill=BOTH, expand=True)

# Create a Text widget and a Scrollbar widget inside the Frame
text_widget = Text(text_frame, height=10, width=40)
scrollbar = Scrollbar(text_frame, command=text_widget.yview)

# Link them together
text_widget.config(yscrollcommand=scrollbar.set)

# Pack scrollbar and text inside their Frame container
scrollbar.pack(side=RIGHT, fill=Y)
text_widget.pack(side=LEFT, fill=BOTH, expand=True)

# Populate text to enable scrolling
for i in range(1, 100):
    text_widget.insert(END, f"This is row number {i}\n")

# Pack the button directly into the main root window, below the Frame
btn = Button(root, text="Check Scroll Position", command=print_scrollbar_position)
btn.pack(side=BOTTOM, pady=10)

root.mainloop()
