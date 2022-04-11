class Account:
    def __init__(self, name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds")
            
    def statement(self):
        print("Account Balance: GHC{}".format(self.balance))
        
    def __str__(self):
        return "{}' Current Account: Balance GHC{}".format(self.name,self.balance)

class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = -1000)
        
class Savings(Account):
    def __init__(self, name,balance):
        super().__init__(name,balance, min_balance = 0)
    
    def __str__(self):
        return "{}' Current Account: Balance GHC{}".format(self.name,self.balance)
        
Alexis = Current("Alexis", 35000 )
Alexis.deposit(200)
Alexis.statement()
Alexis.withdraw(35900)
Alexis.statement()
print(Alexis)

Jude = Savings("Jude",1000)
Jude.deposit(500)
Jude.statement()
Jude.withdraw(5000)
print(Jude)