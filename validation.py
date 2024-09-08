import tkinter as tk

def validate_mass(x):
    try:
        mass_value = x.get()
        if mass_value < 0:
            raise ValueError("Mass cannot be negative")
    except tk.TclError:
        # Handle the case where the user hasn't entered a valid number
        print("Invalid input. Please enter a valid number.")