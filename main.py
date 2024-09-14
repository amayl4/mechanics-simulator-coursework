import tkinter as tk
import vars.validation as vl
from tkinter import ttk

# Main window
window = tk.Tk()
window.title("Mechanics Simulator")  # Title
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
    frame = tk.Frame(window)

    title_label = tk.Label(frame, text="Mechanics Simulator", font=("Helvetica Bold", 36), fg="white")
    title_label.pack(pady=20)

    select_label = tk.Label(frame, text="Select a module", font=("Helvetica Bold", 24), fg="white")
    select_label.pack(pady=20)

    collisions_button = ttk.Button(frame, text="Collisions", style="BW.TButton", command=lambda: switch_frame(collisions_page()))
    collisions_button.pack()

    springs_button = ttk.Button(frame, text="Springs and strings", style="BW.TButton", command=lambda: switch_frame(springs_page()))
    springs_button.pack()
    return frame

# Frame for the collision page
import vars.variables as va

def collisions_page():
    frame = tk.Frame(window)
    label = tk.Label(frame, text="Collisions Page", font=("Helvetica Bold", 24), fg="white")
    label.pack(pady=20)

    m = va.mass(frame)
    m2 = va.mass2(frame)
    u = va.velocity_init(frame)
    u2 =  va.velocity_init2(frame)
    v = va.velocity(frame)
    v2 = va.velocity2(frame)
    e = va.coefficient_restitution(frame)
    i1 = va.impulse1(frame)
    i2 = va.impulse2(frame)

    def validate():
        vl.validate_mass(m)
        vl.validate_mass(m2)
        vl.validate_velocity(u)
        vl.validate_velocity(u2)
        vl.validate_velocity(v)
        vl.validate_velocity(v2)
        vl.validate_restitution(e)
        vl.validate_impulse(i1)
        vl.validate_impulse(i2)

    back_button = ttk.Button(frame, text="Back to main menu", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(padx=10)

    submit_button = ttk.Button(frame, text="Submit", style="BW.TButton", command=lambda: validate())
    submit_button.pack(padx=10)
    return frame

# Frame for the springs page
def springs_page():
    frame = tk.Frame(window)
    label = tk.Label(frame, text="Springs and Strings Page", font=("Helvetica Bold", 24), fg="white")
    label.pack(pady=20)

    m = va.mass(frame)
    k = va.spring_constant(frame)
    s = va.displacement(frame)
    λ = va.young_mod(frame)
    v = va.velocity(frame)
    l = va.natural_length(frame)

    def validate():
        vl.validate_mass(m)
        vl.validate_displacement(s)
        vl.validate_natural_length(l)
        vl.validate_young_modulus(λ)
        vl.validate_velocity(v)
        vl.validate_spring_constant(k)

    back_button = ttk.Button(frame, text="Back to main menu", style="BW.TButton", command=lambda: switch_frame(main_page()))
    back_button.pack(padx=10)

    submit_button = ttk.Button(frame, text="Submit", style="BW.TButton", command=lambda: validate())
    submit_button.pack(padx=10)

    return frame

# Switch to the main page
switch_frame(main_page())
window.mainloop()
