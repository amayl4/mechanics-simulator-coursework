import tkinter as tk
import vars.validation as vl


def mass(x):
    # Create a variable to store the mass value
    mass_var = tk.DoubleVar()
    # Create a label to display the text "Enter mass for particle 1"
    mass_label = tk.Label(x, text="Enter mass for particle 1", font=("Helvetica", 18))
    # Create an entry field to input the mass value
    mass_entry = tk.Entry(x, textvariable=mass_var, font=("Helvetica", 18))
    # Add the entry field to the GUI
    mass_label.pack()
    # Add the label to the GUI
    mass_entry.pack()
    # Return the parent widget with the added mass input component
    return mass_var

def mass2(x):
        mass2_var = tk.DoubleVar()
        mass2_label = tk.Label(x, text="Enter mass for particle 2", font=("Helvetica", 18))
        mass2_entry = tk.Entry(x, textvariable=mass2_var, font=("Helvetica", 18))
        mass2_label.pack()
        mass2_entry.pack()
        return mass2_var

def velocity_init(x):
        initialvel_var = tk.DoubleVar()
        initialvel_label = tk.Label(x, text="Enter initial velocity for particle 1", font=("Helvetica", 18))
        initialvel_entry = tk.Entry(x, textvariable=initialvel_var, font=("Helvetica", 18))
        initialvel_label.pack()
        initialvel_entry.pack()
        return initialvel_var

def velocity_init2(x):
        initialvel2_var = tk.DoubleVar()
        initialvel2_label = tk.Label(x, text="Enter initial velocity for particle 2", font=("Helvetica", 18))
        initialvel2_entry = tk.Entry(x, textvariable=initialvel2_var, font=("Helvetica", 18))
        initialvel2_label.pack()
        initialvel2_entry.pack()
        return initialvel2_var

def velocity(x):
        velocity_var = tk.DoubleVar()
        velocity_label = tk.Label(x, text="Enter (final) velocity for particle 1", font=("Helvetica", 18))
        velocity_entry = tk.Entry(x, textvariable=velocity_var, font=("Helvetica", 18))
        velocity_label.pack()
        velocity_entry.pack()
        return velocity_var

def velocity2(x): 
        velocity2_var = tk.DoubleVar()
        velocity2_label = tk.Label(x, text="Enter (final) velocity for particle 2", font=("Helvetica", 18))
        velocity2_entry = tk.Entry(x, textvariable=velocity2_var, font=("Helvetica", 18))
        velocity2_label.pack()
        velocity2_entry.pack()
        return velocity2_var

def coefficient_restitution(x):
        e_var = tk.DoubleVar()
        restitution_label = tk.Label(x, text="Enter coefficient of restitution", font=("Helvetica", 18))
        restitution_entry = tk.Entry(x, textvariable=e_var, font=("Helvetica", 18))
        restitution_label.pack()
        restitution_entry.pack()
        return e_var

def spring_constant(x): 
        k_var = tk.DoubleVar()
        spring_label = tk.Label(x, text="Enter spring constant", font=("Helvetica", 18))
        spring_entry = tk.Entry(x, textvariable=k_var, font=("Helvetica", 18))
        spring_label.pack()
        spring_entry.pack()
        return k_var

def displacement(x):
        displacement_var = tk.DoubleVar()
        displacement_label = tk.Label(x, text="Enter initial displacement from equilibrium", font=("Helvetica", 18))
        displacement_entry = tk.Entry(x, textvariable=displacement_var, font=("Helvetica", 18))
        displacement_label.pack()
        displacement_entry.pack()
        return displacement_var

def natural_length(x):
        natural_length_var = tk.DoubleVar()
        natural_length_label = tk.Label(x, text="Enter natural length of spring", font=("Helvetica", 18))
        natural_length_entry = tk.Entry(x, textvariable=natural_length_var, font=("Helvetica", 18))
        natural_length_label.pack()
        natural_length_entry.pack()
        return natural_length_var

def young_mod(x):
        mod_var = tk.DoubleVar()
        mod_label = tk.Label(x, text="Enter the Young's Modulus", font=("Helvetica", 18))
        mod_entry = tk.Entry(x, textvariable=mod_var, font=("Helvetica", 18))
        mod_label.pack()
        mod_entry.pack()
        return mod_var

def impulse1(x):
        imp_var = tk.DoubleVar()
        imp_label = tk.Label(x, text="Enter the impulse", font=("Helvetica", 18))
        imp_entry = tk.Entry(x, textvariable=imp_var, font=("Helvetica", 18))
        imp_label.pack()
        imp_entry.pack()
        return imp_var

def impulse2(x):
        imp2_var = tk.DoubleVar()
        imp2_label = tk.Label(x, text="Enter the impulse", font=("Helvetica", 18))
        imp2_entry = tk.Entry(x, textvariable=imp2_var, font=("Helvetica", 18))
        imp2_label.pack()
        imp2_entry.pack()
        return imp2_var