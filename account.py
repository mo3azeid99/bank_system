class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions
