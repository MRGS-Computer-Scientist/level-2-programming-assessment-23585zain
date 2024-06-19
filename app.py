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

        # Input fields
        self.income_var = tk.StringVar()
        self.name_var = tk.StringVar()  
        self.spent_var = tk.StringVar()

        tk.Label(self.root, text="Insert Your Income").grid(row=1, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.income_var).grid(row=1, column=1, pady=5)

        tk.Label(self.root, text="Insert Your Name").grid(row=2, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.name_var).grid(row=2, column=1, pady=5)

        tk.Label(self.root, text="Insert Your Spent Amount").grid(row=4, column=0, sticky="e")
        tk.Entry(self.root, textvariable=self.spent_var).grid(row=4, column=1, pady=5)

        # Calculation section
        self.income_label = tk.Label(self.root, text="Income: $0.00")
        self.income_label.grid(row=5, column=0, columnspan=2, pady=5)

        self.spent_label = tk.Label(self.root, text="Spent: 0%")
        self.spent_label.grid(row=6, column=0, columnspan=2, pady=5)

        self.available_label = tk.Label(self.root, text="Available: $0.00")
        self.available_label.grid(row=7, column=0, columnspan=2, pady=5)

        self.spent_amount_label = tk.Label(self.root, text="Spent: $0.00")
        self.spent_amount_label.grid(row=8, column=0, columnspan=2, pady=5)

        # Optional fixed expenses
        tk.Label(self.root, text="Optionals").grid(row=9, column=0, columnspan=2, pady=10)

        self.expenses = {
            "Netflix": tk.BooleanVar(),
            "Spotify": tk.BooleanVar(),
            "Amazon": tk.BooleanVar(),
            "Google": tk.BooleanVar(),
            "Facebook": tk.BooleanVar()
        }

        row = 10
        for expense, var in self.expenses.items():
            tk.Checkbutton(self.root, text=expense, variable=var).grid(row=row, column=0, columnspan=2, sticky="w")
            row += 1

        # Buttons
        tk.Button(self.root, text="Start Your Calculation", command=self.calculate).grid(row=row, column=0, pady=10)
        tk.Button(self.root, text="Reset Expenses", command=self.reset_expenses).grid(row=row, column=1, pady=10)

    def calculate(self):
        try:
            income = float(self.income_var.get())
            spent = float(self.spent_var.get())

            # Check if the income is greater than $10
            if income <= 10:
                raise ValueError("The minimum income should be more than $10.")

            available = income - spent
            spent_percentage = (spent / income) * 100

            self.income_label.config(text=f"Income: ${income:.2f}")
            self.spent_label.config(text=f"Spent: {spent_percentage:.0f}%")
            self.available_label.config(text=f"Available: ${available:.2f}")
            self.spent_amount_label.config(text=f"Spent: ${spent:.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def reset_expenses(self):
        self.income_var.set("")
        self.name_var.set("")
        self.spent_var.set("")

        self.income_label.config(text="Income: $0.00")
        self.spent_label.config(text="Spent: 0%")
        self.available_label.config(text="Available: $0.00")
        self.spent_amount_label.config(text="Spent: $0.00")

        for var in self.expenses.values():
            var.set(False)

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()