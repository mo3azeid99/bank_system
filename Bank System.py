import tkinter as tk
from tkinter import messagebox, simpledialog
from bank import Bank

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("400x400")
        self.bank = Bank()
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to the Banking System", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.root, text="Open New Account", command=self.create_account, width=30).pack(pady=5)
        tk.Button(self.root, text="Access Existing Account", command=self.access_account, width=30).pack(pady=5)
        tk.Button(self.root, text="Admin Menu", command=self.admin_menu, width=30).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=30).pack(pady=5)

    def admin_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Admin Menu", font=("Arial", 14)).pack(pady=10)

        def delete_account():
            acc_num = simpledialog.askstring("Delete Account", "Enter account number to delete:")
            if acc_num:
                if self.bank.delete_account(acc_num):
                    self.bank.save_data()
                    messagebox.showinfo("Success", "Account deleted successfully!")
                else:
                    messagebox.showerror("Error", "Account not found.")
            else:
                messagebox.showerror("Error", "Account number cannot be empty.")

        tk.Button(self.root, text="Delete Account", command=delete_account).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def create_account(self):
        self.clear_window()
        tk.Label(self.root, text="Open New Account", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Account Number:").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()

        tk.Label(self.root, text="4-Digit PIN:").pack()
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()

        tk.Label(self.root, text="Initial Balance:").pack()
        balance_entry = tk.Entry(self.root)
        balance_entry.pack()

        def submit():
            acc_num = acc_entry.get()
            pin = pin_entry.get()
            balance = balance_entry.get()
            if acc_num and pin.isdigit() and len(pin) == 4 and balance.isdigit():
                if self.bank.create_account(acc_num, pin, float(balance)):
                    self.bank.save_data()
                    messagebox.showinfo("Success", "Account Created Successfully!")
                    self.main_menu()
                else:
                    messagebox.showerror("Error", "Account already exists!")
            else:
                messagebox.showerror("Error", "Invalid input! Please check your entries.")

        tk.Button(self.root, text="Create Account", command=submit).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def access_account(self):
        self.clear_window()
        tk.Label(self.root, text="Login to Your Account", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Account Number:").pack()
        acc_entry = tk.Entry(self.root)
        acc_entry.pack()

        tk.Label(self.root, text="4-Digit PIN:").pack()
        pin_entry = tk.Entry(self.root, show="*")
        pin_entry.pack()

        def login():
            acc_num = acc_entry.get()
            pin = pin_entry.get()
            if acc_num and pin:
                account = self.bank.get_account(acc_num, pin)
                if account:
                    self.user_dashboard(account)
                else:
                    messagebox.showerror("Error", "Invalid account number or PIN.")
            else:
                messagebox.showerror("Error", "Both fields are required.")

        tk.Button(self.root, text="Login", command=login).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def user_dashboard(self, account):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome, {account.account_number}", font=("Arial", 14)).pack(pady=10)

        def check_balance():
            messagebox.showinfo("Balance", f"Your balance is: {account.get_balance()}")

        def deposit():
            amount = simpledialog.askfloat("Deposit", "Enter deposit amount:")
            if amount and amount > 0:
                account.deposit(amount)
                self.bank.save_data()
                messagebox.showinfo("Success", "Deposit successful!")
            else:
                messagebox.showerror("Error", "Invalid deposit amount.")

        def withdraw():
            amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:")
            if amount and amount > 0:
                if account.withdraw(amount):
                    self.bank.save_data()
                    messagebox.showinfo("Success", "Withdrawal successful!")
                else:
                    messagebox.showerror("Error", "Insufficient balance.")
            else:
                messagebox.showerror("Error", "Invalid withdrawal amount.")

        def view_transactions():
            transactions = "\n".join(account.get_transactions())
            if transactions:
                messagebox.showinfo("Transaction History", transactions)
            else:
                messagebox.showinfo("Transaction History", "No transactions yet.")

        tk.Button(self.root, text="Check Balance", command=check_balance).pack(pady=5)
        tk.Button(self.root, text="Deposit Money", command=deposit).pack(pady=5)
        tk.Button(self.root, text="Withdraw Money", command=withdraw).pack(pady=5)
        tk.Button(self.root, text="Transaction History", command=view_transactions).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.main_menu).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()