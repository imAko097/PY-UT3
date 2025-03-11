class Contador:
    # Constructor
    def __init__(self, value):
        self.value = value
    
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