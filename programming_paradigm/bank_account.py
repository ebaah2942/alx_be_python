class BankAccount:
    def __init__(self, current_balance=0):
    
        self.current_balance = current_balance


    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposited: ${amount}")
          

    def withdraw(self, amount):
        if amount > self.current_balance:
            print("Insufficient funds")
            return False
        else:    
            self.current_balance -= amount
            print(f"Withdrew: ${amount}")
            return True

   
    
    def display_balance(self):
        print(f"Current balance: ${self.current_balance:.2f}")


BankAccount(200)       

