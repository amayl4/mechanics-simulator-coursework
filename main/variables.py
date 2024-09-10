import tkinter as tk
import validation as vl

def mass(x):
    # Create a variable to store the mass value
    mass_var = tk.DoubleVar()
    # Create a label to display the text "Enter mass for particle 1"
    mass_label = tk.Label(x, text="Enter mass for particle 1", font=("Helvetica", 18))
    # Create an entry field to input the mass value
    mass_entry = tk.Entry(x, textvariable=mass_var, font=("Helvetica", 18))
    # Add the entry field to the GUI
    mass_entry.pack()
    # Add the label to the GUI
    mass_label.pack()
    # Return the parent widget with the added mass input component
    return mass_var

def mass2(x):
    mass2_var = tk.DoubleVar()
    mass2_label = tk.Label(x, text="Enter mass for particle 2", font=("Helvetica", 18))
    mass2_entry = tk.Entry(x, textvariable=mass2_var, font=("Helvetica", 18))
    mass2_entry.pack()
    mass2_label.pack()
    return mass2_var

def velocity(x):
    velocity_var = tk.DoubleVar()
    velocity_label = tk.Label(x, text="Enter velocity for particle 1", font=("Helvetica", 18))
    velocity_entry = tk.Entry(x, textvariable=velocity_var, font=("Helvetica", 18))
    velocity_entry.pack()
    velocity_label.pack()
    return velocity_var

def velocity2(x): 
    velocity2_var = tk.DoubleVar()
    velocity2_label = tk.Label(x, text="Enter velocity for particle 2", font=("Helvetica", 18))
    velocity2_entry = tk.Entry(x, textvariable=velocity2_var, font=("Helvetica", 18))
    velocity2_entry.pack()
    velocity2_label.pack()
    return velocity2_var

def coefficient_restitution(x):
    e_var = tk.DoubleVar()
    restitution_label = tk.Label(x, text="Enter coefficient of restitution", font=("Helvetica", 18))
    restitution_entry = tk.Entry(x, textvariable=e_var, font=("Helvetica", 18))
    restitution_entry.pack()
    restitution_label.pack()
    return e_var

def spring_constant(x): 
    k_var = tk.DoubleVar()
    spring_label = tk.Label(x, text="Enter spring constant", font=("Helvetica", 18))
    spring_entry = tk.Entry(x, textvariable=k_var, font=("Helvetica", 18))
    spring_entry.pack()
    spring_label.pack()
    return k_var

def displacement(x):
    displacement_var = tk.DoubleVar()
    displacement_label = tk.Label(x, text="Enter initial displacement from equilibrium", font=("Helvetica", 18))
    displacement_entry = tk.Entry(x, textvariable=displacement_var, font=("Helvetica", 18))
    displacement_entry.pack()
    displacement_label.pack()
    return displacement_var

def natural_length(x):
    natural_length_var = tk.DoubleVar()
    natural_length_label = tk.Label(x, text="Enter natural length of spring", font=("Helvetica", 18))
    natural_length_entry = tk.Entry(x, textvariable=natural_length_var, font=("Helvetica", 18))
    natural_length_entry.pack()
    natural_length_label.pack()
    return natural_length_var

def damping_coefficient(x):
    damping_var = tk.DoubleVar()
    damping_label = tk.Label(x, text="Enter the damping coefficient", font=("Helvetica", 18))
    damping_entry = tk.Entry(x, textvariable=damping_var, font=("Helvetica", 18))
    damping_entry.pack()
    damping_label.pack()
    return damping_var

