########################
#### Anas Zughayyar ####
########################
### Assignment: User ###
########################

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User:" , self.name , ", Balance:", self.account_balance)
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount
        return self

anas = User("Anas Zughayyar", "anas@axsos.academy")
omar = User("Omar Rayyan" , "omar@axsos.academy")
sami = User("Sami Dharaghmi", "sami@axsos.academy")

anas.make_deposit(100).make_deposit(50).make_deposit(80).make_withdrawal(200)
print("Anas's account balance =", anas.account_balance)

omar.make_deposit(1000).make_deposit(300).make_withdrawal(700).make_withdrawal(200)
print("Omar's account balance =", omar.account_balance)

sami.make_deposit(200).make_withdrawal(400).make_withdrawal(100).make_withdrawal(50)
print("Sami's account balance =", sami.account_balance)

omar.transfer_money(sami,400).make_deposit(1000)
print("Omar's account balance =", omar.account_balance)
print("Sami's account balance =", sami.account_balance)