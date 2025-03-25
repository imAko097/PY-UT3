# This class represents a bank interface where the user can perform operations on the bank account
class BankInterface:
    # Constructor
    def __init__(self, bank_account):
        self.DEPOSIT_MONEY = 1
        self.WITHDRAW_MONEY = 2
        self.ACCOUNT_INFO = 3
        self.EXIT = 4
    