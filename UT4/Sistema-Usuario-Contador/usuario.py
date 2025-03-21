from contador import Contador
import random

class Usuario:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.fails = Contador(0)
        self.successes = Contador(0)

    # Get the name of the user
    def getName(self):
        return self.name
    
    # Get the number of fails
    def getFails(self):
        return self.fails.getContador()
    
    # Get the number of successes
    def getSuccesses(self):
        return self.successes.getContador()
    
    # Try to login
    def access(self):
        if random.randint(1, 2) == 1:
            self.fails.increment()
        else:
            self.successes.increment()
    
    # Print the user's statistics
    def printStatistics(self):
        print("User: ", self.name)
        print("Fails: ", self.fails.getContador())
        print("Successes: ", self.successes.getContador())
