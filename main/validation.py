import tkinter as tk

def validate_mass(x):
    try:
        mass_value = float(x.get())
        if mass_value < 0 and mass_value is not float:
            raise ValueError("Mass cannot be negative")
    except ValueError as e:
        # Handle the case where the user hasn't entered a valid number or a negative number
        print(f"Invalid input: {e}")
    except tk.TclError:
        # Handle the case where the user hasn't entered a valid number
        print("Invalid input. Please enter a valid number.")

def validate_velocity(x):
    try:
        velocity_value = float(x.get())
        if velocity_value is not float:
            raise ValueError("Velocity must be a real number")
    except ValueError as e:
        # Handle the case where the user hasn't entered a valid number or a negative number
        print(f"Invalid input: {e}")
    except tk.TclError:
        # Handle the case where the user hasn't entered a valid number
        print("Invalid input. Please enter a valid number.")
