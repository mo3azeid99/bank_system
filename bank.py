import json
from account import Account

class Bank:
    def __init__(self, data_file='bank_data.json'):
        self.accounts = {}
        self.data_file = data_file
        self.load_data()

    def create_account(self, account_number, pin, initial_balance):
        if account_number in self.accounts:
            return False  
        self.accounts[account_number] = Account(account_number, pin, initial_balance)
        self.save_data()
        return True

    def get_account(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            self.save_data()
            return True
        return False

    def save_data(self):
        data = {
            acc: {
                "pin": self.accounts[acc].pin,
                "balance": self.accounts[acc].balance,
                "transactions": self.accounts[acc].transactions
            }
            for acc in self.accounts
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for acc, info in data.items():
                    self.accounts[acc] = Account(acc, info["pin"], info["balance"])
                    self.accounts[acc].transactions = info["transactions"]
        except FileNotFoundError:
            pass  
