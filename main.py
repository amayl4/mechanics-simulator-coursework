import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Mechanics Simulator")
window.configure(bg="black")
window.geometry("800x600")

current_frame = None

def switch_frame(frame):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
    current_frame = frame
    current_frame.pack(fill='both', expand=True)

def main_page():
    frame = tk.Frame(window, bg="black")

    title_label = tk.Label(frame, text="Mechanics Simulator", font=("Times New Roman", 36), bg="black", fg="white")
    title_label.pack(pady=20)

    select_label = tk.Label(frame, text="Select a module", font=("Times New Roman", 24), bg="black", fg="white")
    select_label.pack()
    
    button_frame = tk.Frame(frame, bg="black")
    button_frame.pack(pady=20)
    
    impulse_button = ttk.Button(button_frame, text="Impulse and Work Done", style="BW.TButton", command=lambda: switch_frame(impulse_page()))
    impulse_button.pack(pady=10)
    style1 = ttk.Style()
    style1.configure("BW.TButton", font=("Times New Roman", 18))

    collisions_button = ttk.Button(button_frame, text="Collisions", style="BW.TButton", command=lambda: switch_frame(collisions_page()))
    collisions_button.pack(pady=10)
    
    kinematics_button = ttk.Button(button_frame, text="Kinematics and Dynamics", style="BW.TButton", command=lambda: switch_frame(kinematics_page()))
    kinematics_button.pack(pady=10)
    
    return frame
def impulse_page():
    frame = tk.Frame(window, bg="black")
    
    label = tk.Label(frame, text="Welcome to the Impulse and Work Done page!", font=("Times New Roman", 24), bg="black", fg="white")
    label.pack(pady=20)
    
    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    impulse1D = ttk.Button(frame, text="Impulse-momentum in 1D", style="BW.TButton", command=lambda: switch_frame())
    impulse1D.pack(pady=10)

    impulse2D = ttk.Button(frame, text="Impulse-momentum in 2D", style="BW.TButton", command=lambda: switch_frame())
    impulse2D.pack(pady=10)

    work_energy = ttk.Button(frame, text="Work, energy and power", style="BW.TButton", command=lambda: switch_frame())
    work_energy.pack(pady=10)

    springs = ttk.Button(frame, text="Elastic springs/strings", style="BW.TButton", command=lambda: switch_frame())
    springs.pack(pady=10)

    return frame

def collisions_page():
    frame = tk.Frame(window, bg="black")
    
    label = tk.Label(frame, text="Welcome to the Collisions page!", font=("Times New Roman", 24), bg="black", fg="white")
    label.pack(pady=20)
    
    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)
    
    collision1D = ttk.Button(frame, text="Collisions in 1D", style="BW.TButton", command=lambda: switch_frame())
    collision1D.pack(pady=10)

    collision2D = ttk.Button(frame, text="Collisions in 2D", style="BW.TButton", command=lambda: switch_frame())
    collision2D.pack(pady=10)

    return frame

def kinematics_page():
    frame = tk.Frame(window, bg="black")
    
    label = tk.Label(frame, text="Welcome to the Kinematics and Dynamics page!", font=("Times New Roman", 24), bg="black", fg="white")
    label.pack(pady=20)
    
    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    kinematics = ttk.Button(frame, text="Kinematics", style="BW.TButton", command=lambda: switch_frame())
    kinematics.pack(pady=10)

    dynamics = ttk.Button(frame, text="Dynamics", style="BW.TButton", command=lambda: switch_frame())
    dynamics.pack(pady=10)
    
    return frame

switch_frame(main_page())

window.mainloop()