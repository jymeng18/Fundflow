'''Expense Tracker Prototype - Manage your expenses with the innovative envelope system'''

class Envelope:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def load_contents(self):
        print(f"{self.name}: $ {float(self.balance)}\n")
        
    def deposit(self, amount):
        self.balance += amount
        
    def spend(self, amount):
        if amount > self.balance:
            print("Balance not enough!")
        else:
            self.balance -= amount
    
    