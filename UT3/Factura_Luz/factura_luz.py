class FacturaLuz:
    # Constructor
    def __init__(self, kw_consumed):
        if kw_consumed < 0:
            raise ValueError("The consumed kilowatts must be positive")
        self.kw_consumed = kw_consumed
        # Constants
        self.PRICE = 0.086
        self.IVA = 0.16
    
    # Accessor of the consumed kilowatts
    def getKwConsumed(self):
        return self.kw_consumed

    # Calculate the total price of the electricity bill
    def calculatePrice(self):
        return self.kw_consumed * self.PRICE * (1 + self.IVA)