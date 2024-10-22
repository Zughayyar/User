########################
#### Anas Zughayyar ####
########################
##### Bank Account #####
########################

class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("Balance:", self.balance)
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
        return self


anas_account = BankAccount(0.02,1000)
omar_account = BankAccount(0.01,2000)

anas_account.deposit(200).deposit(300).deposit(500).withdraw(700).yield_interest().display_account_info()

omar_account.deposit(200).deposit(500).withdraw(400).withdraw(100).withdraw(400).withdraw(50).yield_interest().display_account_info()

anas_account.withdraw(2000).display_account_info()

