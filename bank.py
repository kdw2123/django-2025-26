class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited: {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds! Withdrawal denied.")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount(500)  

print("Current Balance:", account.get_balance())  

account.deposit(200)        
account.withdraw(100)       

account.withdraw(700)       
account.withdraw(-50)       

print("Final Balance:", account.get_balance())

