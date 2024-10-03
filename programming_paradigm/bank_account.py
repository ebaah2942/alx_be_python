class BankAccount:
    def __init__(self, balance=0):
    
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")
          

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False
        else:    
            self.balance -= amount
            print(f"Withdrawn: ${amount} successfully")
            return True

   
    
    def display_balance(self):
        print(f"Balance: ${self.balance:.2f}")


BankAccount(200)       

