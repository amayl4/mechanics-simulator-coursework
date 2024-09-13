import tkinter as tk

def validate_mass(x):
    try:
        mass_value = float(x.get())
        if mass_value < 0 and mass_value is not float:
            raise ValueError("Mass must be a postitive real number")
    except ValueError as e:
        # Handle the case where the user hasn't entered a valid number or a negative number
        print(f"Invalid input: {e}")

# def validate_mass(x):
#     mass_value = float(x.get())
#     if mass_value < 0 and mass_value is not float:
#         raise ValueError("Mass must be a positive real number")

def validate_velocity(x):
    try:
        velocity_value = float(x.get())
        if velocity_value is not float:
            raise ValueError("Velocity must be a real number")
    except ValueError as e:
        # Handle the case where the user hasn't entered a valid number or a negative number
        print(f"Invalid input: {e}")

def validate_restitution(x):
    try:
        restitution_value = float(x.get())
        if restitution_value < 0 or restitution_value > 1:
            raise ValueError("Restitution coefficient must be between 0 and 1")
    except ValueError as e:
        print(f"Invalid input: {e}")

def validate_displacement(x):  
    try:
        displacement_value = float(x.get())
        if displacement_value < 0:
            raise ValueError("Displacement must be a positive real number")
    except ValueError as e:
        print(f"Invalid input: {e}")

def validate_natural_length(x):  
    try:
        displacement_value = float(x.get())
        if displacement_value < 0:
            raise ValueError("Natural length must be a positive real number")
    except ValueError as e:
        print(f"Invalid input: {e}")

def validate_spring_constant(x):
    try:
        spring_constant_value = float(x.get())
        if spring_constant_value < 0:
            raise ValueError("Spring constant must be a positive real number")
    except ValueError as e:
        print(f"Invalid input: {e}")

def validate_young_modulus(x):
    try:
        spring_constant_value = float(x.get())
        if spring_constant_value < 0:
            raise ValueError("Young's Modulus must be a positive real number")
    except ValueError as e:
        print(f"Invalid input: {e}")