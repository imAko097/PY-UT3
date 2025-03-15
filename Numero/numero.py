class Numero:
    # Constructor
    def __init__(self):
        self.value = 999
    
    # Get
    def get_value(self):
        return self.value

    # Set
    def set_value(self, value):
        if value < 100 or value > 999:
            raise ValueError('Value must be between 100 and 999')
        else:
            self.value = value
    
    # Even
    def is_even(self):
        return self.value % 2 == 0
    
    # Get last digit
    def get_last_digit(self):
        return self.value % 10
    
    # Get the add of the digits
    def get_add_digits(self):
        return self.value // 100 + (self.value // 10) % 10 + self.value % 10
