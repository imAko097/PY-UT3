# This class represents a bank account
class BankAccount:
    # Constructor
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
    
    # Getter method for account number
    def get_account_number(self):
        return self.account_number
    
    # Getter method for balance
    def get_balance(self):
        return self.balance
    
    # Getter method for owner
    def get_owner(self):
        return self.owner
    
    # Method to deposit money
    def deposit(self, amount):
        if amount < 0:
            print("Error: Cannot deposit negative amount")
        else:
            self.balance += amount
            print("Deposited", amount, "into account", self.account_number)
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount < 0:
            print("Error: Cannot withdraw negative amount")
        elif amount > self.balance:
            print("Error: Insufficient funds")
        else:
            self.balance -= amount
            print("Withdrew", amount, "from account", self.account_number)
    
    # Account info
    def __str__(self):
        return "Account Number: " + self.account_number + "\n" + \
                "Balance: " + str(self.balance) + "\n" + \
                "Owner: " + self.owner