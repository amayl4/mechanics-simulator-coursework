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

    impulse1D = ttk.Button(frame, text="Impulse-momentum in 1D", style="BW.TButton", command=lambda: switch_frame(parameter_entry_impuluse1D()))
    impulse1D.pack(pady=10)

    impulse2D = ttk.Button(frame, text="Impulse-momentum in 2D", style="BW.TButton", command=lambda: switch_frame(parameter_entry_collisions2D()))
    impulse2D.pack(pady=10)

    work_energy = ttk.Button(frame, text="Work, energy and power", style="BW.TButton", command=lambda: switch_frame(parameter_entry_workenergy()))
    work_energy.pack(pady=10)

    springs = ttk.Button(frame, text="Elastic springs/strings", style="BW.TButton", command=lambda: switch_frame(parameter_entry_springs()))
    springs.pack(pady=10)

    return frame

def collisions_page():
    frame = tk.Frame(window, bg="black")
    
    label = tk.Label(frame, text="Welcome to the Collisions page!", font=("Times New Roman", 24), bg="black", fg="white")
    label.pack(pady=20)
    
    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)
    
    collision1D = ttk.Button(frame, text="Collisions in 1D", style="BW.TButton", command=lambda: switch_frame(parameter_entry_collisions1D()))
    collision1D.pack(pady=10)

    collision2D = ttk.Button(frame, text="Collisions in 2D", style="BW.TButton", command=lambda: switch_frame(parameter_entry_collisions2D()))
    collision2D.pack(pady=10)

    return frame

def kinematics_page():
    frame = tk.Frame(window, bg="black")
    
    label = tk.Label(frame, text="Welcome to the Kinematics and Dynamics page!", font=("Times New Roman", 24), bg="black", fg="white")
    label.pack(pady=20)
    
    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    kinematics = ttk.Button(frame, text="Kinematics", style="BW.TButton", command=lambda: switch_frame(parameter_entry_kinematics()))
    kinematics.pack(pady=10)

    dynamics = ttk.Button(frame, text="Dynamics", style="BW.TButton", command=lambda: switch_frame(parameter_entry_dynamics()))
    dynamics.pack(pady=10)
    
    return frame

# Entry fields for the parameters
def massA_imp_col1D(x):
    massA_var = tk.IntVar()
    massA_label = tk.Label(x, text="Enter mass for particle 1", font=("Times New Roman", 18))
    massA_entry = tk.Entry(x, textvariable=massA_var, font=("Times New Roman", 18))
    massA_entry.pack()
    massA_label.pack()
    return x

def massB_imp_col1D(x):
    massB_var = tk.IntVar()
    massB_label = tk.Label(x, text="Enter mass for particle 2", font=("Times New Roman", 18))
    massB_entry = tk.Entry(x, textvariable=massB_var, font=("Times New Roman", 18))
    massB_entry.pack()
    massB_label.pack()
    return x

def vA_imp_col1D(x):
    vA_var = tk.IntVar()
    vA_label = tk.Label(x, text="Enter final velocity for particle 1", font=("Times New Roman", 18))
    vA_entry = tk.Entry(x, textvariable=vA_var, font=("Times New Roman", 18))
    vA_entry.pack()
    vA_label.pack()
    return x

def vB_imp_col1D(x):
    vB_var = tk.IntVar()
    vB_label = tk.Label(x, text="Enter final velocity for particle 2", font=("Times New Roman", 18))
    vB_entry = tk.Entry(x, textvariable=vB_var, font=("Times New Roman", 18))
    vB_entry.pack()
    vB_label.pack()
    return x

def uA_imp_col1D(x):
    uA_var = tk.IntVar()
    uA_label = tk.Label(x, text="Enter initial velocity for particle 1", font=("Times New Roman", 18))
    uA_entry = tk.Entry(x, textvariable=uA_var, font=("Times New Roman", 18))
    uA_entry.pack()
    uA_label.pack()
    return x

def uB_imp_col1D(x):
    uB_var = tk.IntVar()
    uB_label = tk.Label(x, text="Enter inital velocity for particle 2", font=("Times New Roman", 18))
    uB_entry = tk.Entry(x, textvariable=uB_var, font=("Times New Roman", 18))
    uB_entry.pack()
    uB_label.pack()
    return x

def timeA_imp_col1D(x):
    timeA_var = tk.IntVar()
    timeA_label = tk.Label(x, text="Enter time taken by particle 1", font=("Times New Roman", 18))
    timeA_entry = tk.Entry(x, textvariable=timeA_var, font=("Times New Roman", 18))
    timeA_entry.pack()
    timeA_label.pack()
    return x

def timeB_imp_col1D(x):
    timeB_var = tk.IntVar()
    timeB_label = tk.Label(x, text="Enter time taken by particle 2", font=("Times New Roman", 18))
    timeB_entry = tk.Entry(x, textvariable=timeB_var, font=("Times New Roman", 18))
    timeB_entry.pack()
    timeB_label.pack()
    return x

def forceA_imp_col1D(x):
    forceA_var = tk.IntVar()
    forceA_label = tk.Label(x, text="Enter force exerted on particle 1", font=("Times New Roman", 18))
    forceA_entry = tk.Entry(x, textvariable=forceA_var, font=("Times New Roman", 18))
    forceA_entry.pack()
    forceA_label.pack()
    return x

def forceB_imp_col1D(x):
    forceB_var = tk.IntVar()
    forceB_label = tk.Label(x, text="Enter force exerted on particle 2", font=("Times New Roman", 18))
    forceB_entry = tk.Entry(x, textvariable=forceB_var, font=("Times New Roman", 18))
    forceB_entry.pack()
    forceB_label.pack()
    return x

# Paramter entry frames
def parameter_entry_impuluse1D():
    frame = tk.Frame(window, bg="black")

    label = tk.Label(frame, text="Enter parameters for 1D impulse", font=("Times New Roman", 18), bg="black", fg="white")
    label.pack(pady=20)

    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)
    
    massA_imp_col1D(frame)
    massB_imp_col1D(frame)
    vA_imp_col1D(frame)
    vB_imp_col1D(frame)
    uA_imp_col1D(frame)
    uB_imp_col1D(frame)
    timeA_imp_col1D(frame)
    timeB_imp_col1D(frame)
    forceA_imp_col1D(frame)
    forceB_imp_col1D(frame)
    return frame



def parameter_entry_impuluse2D():
    frame = tk.Frame(window, bg="black")

    label = tk.Label(frame, text="Enter parameters for 2D impulse", font=("Times New Roman", 18), bg="black", fg="white")
    label.pack(pady=20)

    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    return frame

def parameter_entry_workenergy():
    frame = tk.Frame(window, bg="black")

    label = tk.Label(frame, text="Enter parameters for work-energy problems", font=("Times New Roman", 18), bg="black", fg="white")
    label.pack(pady=20)

    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    return frame

def parameter_entry_springs():
    frame = tk.Frame(window, bg="black")

    label = tk.Label(frame, text="Enter parameters for elastic springs/strings", font=("Times New Roman", 18), bg="black", fg="white")
    label.pack(pady=20)

    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    return frame

def parameter_entry_collisions1D():
    frame = tk.Frame(window, bg="black")

    label = tk.Label(frame, text="Enter parameters for 1D collisions", font=("Times New Roman", 18), bg="black", fg="white")
    label.pack(pady=20)

    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    return frame

def parameter_entry_collisions2D():
    frame = tk.Frame(window, bg="black")

    label = tk.Label(frame, text="Enter parameters for 2D collisions", font=("Times New Roman", 18), bg="black", fg="white")
    label.pack(pady=20)

    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    return frame

def parameter_entry_kinematics():
    frame = tk.Frame(window, bg="black")

    label = tk.Label(frame, text="Enter parameters for kinematics", font=("Times New Roman", 18), bg="black", fg="white")
    label.pack(pady=20)

    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    return frame

def parameter_entry_dynamics():
    frame = tk.Frame(window, bg="black")

    label = tk.Label(frame, text="Enter parameters for dynamics", font=("Times New Roman", 18), bg="black", fg="white")
    label.pack(pady=20)

    back_button = ttk.Button(frame, text="Back to Main Page", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(pady=10)

    return frame

switch_frame(main_page())

window.mainloop()