class Calculadora:
    # Constructor
    def __init__(self):
        self.quantity = 0 # Quantity of numbers
        self.add = 0 # Sum of the numbers
        self.max = 0 # Maximum number
        self.min = 0 # Minimum number

    # Quantity Getter
    def get_quantity(self):
        return self.quantity

    # Add Getter
    def get_add(self):
        return self.add
    
    # Max Getter
    def get_max(self):
        return self.max

    # Min Getter
    def get_min(self):
        return self.min

    # Introduce a number
    def introduce_number(self, number):
        self.quantity += 1 # Increment the quantity

        # If it is the first number, set the add, max and min to the number
        if self.quantity == 1:
            self.add = number
            self.max = number
            self.min = number
        else:
            self.add += number
            # Set the max
            if number > self.max:
                self.max = number
            # Set the min
            if number < self.min:
                self.min = number
    
    # Calculate the average
    def get_average(self):
        return self.add / self.quantity
    
    # Show the current status of the calculator
    def show_status(self):
        print(f"> Quantity: {self.quantity}")
        print(f"> Add: {self.add}")
        print(f"> Max: {self.max}")
        print(f"> Min: {self.min}")
        # Calculate the average
        average = self.get_average()
        print(f"> Average: {round(average, 2)}")