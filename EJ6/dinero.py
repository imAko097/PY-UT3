class Dinero:
    # Constructor
    def __init__(self, money):
        if money >= 1 and money <= 100:
            self.money = money
        else:
            raise ValueError("El dinero debe estar entre 1 y 100")
    
    # Set method
    def setMoney(self, money):
        if money >= 1 and money <= 100:
            self.money = money
        else:
            raise ValueError("El dinero debe estar entre 1 y 100")
    
    # Get method
    def getMoney(self):
        return self.money

    # Display the breakdown of the money stored by the class objects into the minimum number of 10-euro, 5-euro, 2-euro and 1-euro notes
    def printCoinDescomposition(self):
        print("Descomposición de monedas")
        print("Billetes de 10€: ", self.money // 10)
        print("Billetes de 5€: ", (self.money % 10) // 5)
        print("Monedas de 2€: ", ((self.money % 10) % 5) // 2)
        print("Monedas de 1€: ", ((self.money % 10) % 5) % 2)
