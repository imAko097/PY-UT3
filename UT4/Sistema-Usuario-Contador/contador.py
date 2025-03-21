class Contador:
    # Constructor
    def __init__(self, value_or_contador = 0):
        if isinstance(value_or_contador, Contador): # if it is a Contador object
            self.value = value_or_contador.getContador()
        else: # if it is not a Contador object
            self.value = value_or_contador

    # Decrement
    def decrement(self):
        self.value -= 1
    
    # Accessor Contador
    def getContador(self):
        return self.value

    # Increment
    def increment(self):
        self.value += 1
    
    # Print the value of the counter
    def printContador(self):
        print("Counter value: ", self.value)
    
    # Reset the counter
    def reset(self):
        self.value = 0