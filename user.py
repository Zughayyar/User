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

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User:" , self.name , ", Balance:", self.account_balance)
    
    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount


anas = User("Anas Zughayyar", "anas@axsos.academy")
omar = User("Omar Zaid" , "omar@axsos.academy")
sami = User("Sami Dharaghmi", "sami@axsos.academy")

anas.make_deposit(100)
anas.make_deposit(50)
anas.make_deposit(80)
anas.make_withdrawal(200)
print("Anas's account balance =", anas.account_balance)

omar.make_deposit(1000)
omar.make_deposit(300)
omar.make_withdrawal(700)
omar.make_withdrawal(200)
print("Omar's account balance =", omar.account_balance)

sami.make_deposit(200)
sami.make_withdrawal(400)
sami.make_withdrawal(100)
sami.make_withdrawal(50)
print("Sami's account balance =", sami.account_balance)

omar.transfer_money(sami,400)
print("Omar's account balance =", omar.account_balance)
print("Sami's account balance =", sami.account_balance)