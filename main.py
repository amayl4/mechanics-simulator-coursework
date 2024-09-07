import tkinter as tk
from tkinter import ttk

# Main window
window = tk.Tk()
window.title("Mechanics Simulator")  # Title
window.configure(bg="black")  # Background colour
window.geometry("800x800")  # Size of window
current_frame = None

def switch_frame(frame):
    # Switches the current frame to a new one.
    global current_frame 
    if current_frame is not None: 
        current_frame.destroy()
        # Destroys the current frame and packs the new frame.
    current_frame = frame
    current_frame.pack(fill='both', expand=True)

def main_page():
    # Creates the main page frame.
    frame = tk.Frame(window, bg="black")

    title_label = tk.Label(frame, text="Mechanics Simulator", font=("Helvetica", 36), bg="black", fg="white")
    title_label.pack(pady=20)

    select_label = tk.Label(frame, text="Select a module", font=("Helvetica", 24), bg="black", fg="white")
    select_label.pack(pady=20)

    button_frame = tk.Frame(frame, bg="black")
    button_frame.pack()

    collisions_button = ttk.Button(button_frame, text="Collisions", style="BW.TButton", command=lambda: switch_frame(collisions_page()))
    collisions_button.pack(side='left', padx=10)

    springs_button = ttk.Button(button_frame, text="Springs and strings", style="BW.TButton", command=lambda: switch_frame(springs_page()))
    springs_button.pack(side='right', padx=10)
    return frame

# Frame for the collision page
def collisions_page():
    frame = tk.Frame(window, bg="black")
    label = tk.Label(frame, text="Collisions Page", font=("Helvetica", 24), bg="black", fg="white")
    label.pack()
    return frame

# Frame for the springs page
def springs_page():
    frame = tk.Frame(window, bg="black")
    label = tk.Label(frame, text="Springs and Strings Page", font=("Helvetica", 24), bg="black", fg="white")
    label.pack()
    return frame

# Switch to the main page
switch_frame(main_page())
window.mainloop()
