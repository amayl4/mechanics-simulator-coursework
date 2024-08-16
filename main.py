import tkinter as tk
from tkinter import ttk

# main window
window = tk.Tk()
window.title("Mechanics Simulator")
window.configure(bg="black")
window.geometry("800x600")

# Mechanics Simulator title
title_label = tk.Label(window, text="Mechanics Simulator", font=("Times New Roman", 36), bg="black", fg="white")
title_label.pack(pady=20)

# Select a module
select_label = tk.Label(window, text="Select a module", font=("Times New Roman", 24), bg="black", fg="white")
select_label.pack()

