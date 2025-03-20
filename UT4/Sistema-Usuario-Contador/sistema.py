from usuario import Usuario

class Sistema:
    # Constructor; without parameters - three users are created
    def __init__(self):
        self.user1 = Usuario("One")
        self.user2 = Usuario("Two")
        self.user3 = Usuario("Three")
    
    # Simulate the access of the users
    def simulateAccess(self):
        self.user1.access()
        self.user2.access()
        self.user3.access()
    
    # Print the statistics of the users
    def printStatistics(self):
        self.user1.printStatistics()
        self.user2.printStatistics()
        self.user3.printStatistics()