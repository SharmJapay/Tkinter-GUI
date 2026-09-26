import tkinter as tk

root = tk.Tk()
root.title("Fixed Left, Responsive Right (Pack)")
root.geometry("600x300")

# Left Frame: Fixed size
left_frame = tk.Frame(root, bg="lightblue", width=150)
left_frame.pack_propagate(False)  # Prevents child widgets from changing its size
left_frame.pack(side="left", fill="y", expand=False, padx=5, pady=5)

# Right Frame: Dynamically fills remaining space
right_frame = tk.Frame(root, bg="lightgreen")
right_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Add contents
tk.Label(left_frame, text="Sidebar (150px)", bg="lightblue").pack(pady=10)
tk.Label(right_frame, text="Main Content (Responsive)", bg="lightgreen").pack(pady=10)

root.mainloop()
