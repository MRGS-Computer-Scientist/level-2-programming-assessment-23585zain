import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Yourself")
        self.create_widgets()

    def create_widgets(self): 
        # Title
        title = tk.Label(self.root, text="Budget Yourself", font=("Helvetica", 18, "bold"), fg="brown")
        title.grid(row=0, column=0, columnspan=2, pady=10) 
 