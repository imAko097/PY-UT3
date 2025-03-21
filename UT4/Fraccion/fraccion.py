class Fraccion:
    def __init__(self, numerator, denominator = 1):
        if denominator == 0:
            raise ValueError("The denominator can't be zero")
        
        self.numerator = numerator
        self.denominator = denominator
        
    # Numerator getter
    def get_numerator(self):
        return self.numerator
    
    # Denominator getter
    def get_denominator(self):
        return self.denominator
    
    # Numerator setter
    def set_numerator(self, numerator):
        self.numerator = numerator

    # Denominator setter
    def set_denominator(self, denominator):
        if denominator == 0:
            raise ValueError("The denominator can't be zero")
        
        self.denominator = denominator
    
    # Add two fractions
    def add(self, other):
        if not isinstance(other, Fraccion):
            raise TypeError("The object must be a fraction")

        if self.denominator == other.denominator:
            return Fraccion(self.numerator + other.numerator, self.denominator)
        
        return Fraccion(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
    
    # Subtract two fractions
    def subtract(self, other):
        if not isinstance(other, Fraccion):
            raise TypeError("The object must be a fraction")

        if self.denominator == other.denominator:
            return Fraccion(self.numerator - other.numerator, self.denominator)
        
        return Fraccion(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
    
    # String representation
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"