class BankAccount:
    
    accounts = []

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance - 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest-rate: {self.int_rate}")
        return self
    
    def yield_interest(self):
        if self.balance <= 0:
            print(f"There are insufficient funds. You cannot gain interest.")
        else:
            self.balance += self.balance * self.int_rate
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


account1 = BankAccount(0.05, 100)
account2 = BankAccount(0.03, 300)
# First account activity
account1.deposit(200).deposit(100).deposit(300).withdraw(600).yield_interest().display_account_info()
account2.deposit(300).deposit(400).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()
print("")

BankAccount.display_all_accounts()
