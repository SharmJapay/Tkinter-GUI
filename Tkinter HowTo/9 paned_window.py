"""This file shows How to create paned window Tkinter app"""

# Let us discuss a few of the important ones that you will want to use often.

# 1) parent: The compulsory first parameter required in every tkinter widget. Specifies the container in which the widget will be stored.
# 2) sashrelief: This can be used to change the look of the “sash” which divides a window into multiple panes. If you are on Windows, then make sure to keep this value to tk.RAISED, else the draggable sash will not be visible.
# 3) showhandle: Displays a small “handle” in the form of a square on the sash.
# 4) width: Size in pixels (horizontally)
# 5) height: Size in pixels (vertically)

import tkinter as tk
import tkinter.ttk as ttk


class Window:
    """Object that divides window vertically"""

    def __init__(self, master):
        mainpanel = tk.PanedWindow(
            master, sashrelief=tk.RAISED, showhandle=True, width=300, height=300
        )
        mainpanel.pack(fill=tk.BOTH, expand=True)

        label_1 = tk.Label(mainpanel, text="Main Panel")
        label_2 = tk.Label(mainpanel, text="Other Text")
        mainpanel.add(label_1)
        mainpanel.add(label_2)


root = tk.Tk()
window = Window(root)
root.mainloop()


# Secondly, we added the stretch option into our add() functions. This is rather similar to expand and fill used in pack(). The stretch parameter can take the following possible values:

# 1) always: This pane will always stretch (expand and occupy available space).
# 2) first: Stretch only if this pane is the first pane (left-most or top-most) .
# 3) last: Stretch only if this pane is the last pane (right-most or bottom-most). This is the default value.
# 4) middle: Stretch only if this pane is not the first or last pane.
# 5) never: This pane will never stretch.


class Window1:
    """Object that divides window horizontally"""

    def __init__(self, master):
        mainpanel = tk.PanedWindow(
            master,
            orient=tk.VERTICAL,
            sashrelief=tk.RAISED,
            showhandle=True,
            width=300,
            height=300,
        )
        mainpanel.pack(fill=tk.BOTH, expand=True)

        label_1 = tk.Label(mainpanel, text="Main Panel")
        label_2 = tk.Label(mainpanel, text="Other Text")
        mainpanel.add(label_1, stretch="always")
        mainpanel.add(label_2, stretch="always")


root1 = tk.Tk()
window1 = Window1(root1)
root1.mainloop()


# Here is a slightly more complex example with nested PanedWindows. We create a “subpanel”, add a widget or two into it, then add into the mainpanel just like we would to any other widget.


class Window2:
    """Object that divides window horizontally and vertically"""

    def __init__(self, master):
        ttk.Style().theme_use("classic")
        mainpanel = tk.PanedWindow(
            master, sashrelief=tk.RAISED, showhandle=True, width=300, height=300
        )
        mainpanel.pack(fill=tk.BOTH, expand=True)

        label_0 = tk.Label(mainpanel, text="Main Panel")
        mainpanel.add(label_0)

        subpanel_1 = tk.PanedWindow(mainpanel, sashrelief=tk.RAISED, orient=tk.VERTICAL)
        mainpanel.add(subpanel_1)

        label_1 = tk.Label(subpanel_1, text="Sub Panel 1")
        label_2 = tk.Label(subpanel_1, text="Sub Panel 2")
        subpanel_1.add(label_1)
        subpanel_1.add(label_2)


root2 = tk.Tk()
window2 = Window2(root2)
root2.mainloop()
