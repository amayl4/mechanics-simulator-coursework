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
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    select_label = tk.Label(frame, text="Select a module", font=("Helvetica", 24), bg="black", fg="white")
    select_label.grid(row=1, column=0, columnspan=2)

    # Uses command = lambda: f(x) to provide the functionality
    collisions_button = ttk.Button(frame, text="Collisions", style="BW.TButton", command=lambda: switch_frame(collisions_page()))
    collisions_button.grid(row=2, column=0, padx=(20, 10))

    springs_button = ttk.Button(frame, text="Springs and strings", style="BW.TButton", command=lambda: switch_frame(springs_page()))
    springs_button.grid(row=2, column=1, padx=(10, 20))

    style1 = ttk.Style()
    style1.configure("BW.TButton", font=("Helvetica", 18))
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
