# Modela el comportamiento de una hucha que guarda una determinada amount de money. Podemos meter o sacar money de ella.
class Hucha:
    # Constructor
    def __init__(self):
        self.money = 0
    
    # How much money is in the piggy bank
    def getMoney(self):
        return self.money
    
    # Put money in
    def putMoney(self, amount):
        if amount > 0:
            self.money += amount
        else:
            print("Error: amount must be greater than 0")
    
    # Take money out
    def takeMoney(self, amount):
        if amount > 0:
            if amount <= self.money:
                self.money -= amount
            else:
                print("No enough money in the piggy bank. You take out all the money!")
                self.money = 0
        else:
            print("Error: amout must be greater than 0")
    
    # Print the amount of money in the piggy bank
    def printMoney(self):
        print("Money in the piggy bank: ", self.money, " euros")
