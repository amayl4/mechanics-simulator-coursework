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

# On-click function
def on_click(button_name): # Takes the name of the button as a parameter
    print(f"{button_name} has been selected") # Prints the action to the console


# Create new page function
def new_page(button_name):
    new_window = tk.Toplevel(window)
    new_window.title(f"{button_name}")
    new_window.configure(bg="black")

    label = tk.Label(new_window, text=f"Welcome to the {button_name} page!", font=("Times New Roman", 24), bg="black", fg="white")
    label.pack(pady=20)

    # Add a button to go back to the main page
    back_button = ttk.Button(new_window, text="Back to Main Page", style="BW.TButton", command=new_window.destroy)
    back_button.pack(pady=10)

# Buttons ~ Impulse, Collisions, Kinematics and Dynamics
impulse_button = ttk.Button(button_frame, text="Impulse and Work Done", style="BW.TButton", command=lambda: on_click("Impulse and Work Done"), comm = new_page("Impulse and Work Done"))
impulse_button.pack(pady=10)

collisions_button = ttk.Button(button_frame, text="Collisions", style="BW.TButton", command=lambda: on_click("Collisions"))
collisions_button.pack(pady=10)

kinematics_button = ttk.Button(button_frame, text="Kinematics and Dynamics", style="BW.TButton", command=lambda: on_click("Kinematics and Dynamics"))
kinematics_button.pack(pady=10)

# Style for buttons
style = ttk.Style()
style.configure("BW.TButton", background="black", foreground="white", font=("Times New Roman", 18))

# Main loop
window.mainloop()