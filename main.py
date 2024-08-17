import tkinter as tk
from tkinter import ttk

# main window
window = tk.Tk()
window.title("Mechanics Simulator")
window.configure(bg="black") # Background colour
window.geometry("800x600") # Size of the window

# Mechanics Simulator title
title_label = tk.Label(window, text="Mechanics Simulator", font=("Times New Roman", 36), bg="black", fg="white")
title_label.pack(pady=20)

# Select a module
select_label = tk.Label(window, text="Select a module", font=("Times New Roman", 24), bg="black", fg="white")
select_label.pack()

# Button frame
button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=20)

# Buttons ~ Impulse, Collisions, Kinematics and Dynamics
impulse_button = ttk.Button(button_frame, text="Impulse and Work Done", style="BW.TButton")
impulse_button.pack(pady=10)

collisions_button = ttk.Button(button_frame, text="Collisions", style="BW.TButton")
impulse_button.pack(pady=10)

kinematics_button = ttk.Button(button_frame, text="Kinematics and Dynamics", style="BW.TButton")
impulse_button.pack(pady=10)

# Style for buttons
style = ttk.Style()
style.configure("BW.TButton", background="black", foreground="white", font=("Times New Roman", 18))

# Main loop
window.mainloop()