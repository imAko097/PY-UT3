# Two attributes: name and age of the passenger
class Passenger:
    # Constructor
    def __init__(self, name, age = -1):
        if not isinstance(name, str):
            raise TypeError("The name must be a string")
        if age < 0:
            self.age = -1
        
        self.name = name
        self.age = age

    # Get the name of the passenger
    def get_name(self):
        return self.name

    # Get the age of the passenger
    def get_age(self):
        return self.age
    
    # Info of the passenger
    def __str__(self):
        unknow_age = "Not specified" if self.age == -1 else self.age
        return f"Name: {self.name}\nAge: {unknow_age}"

    # More young than other passenger
    def __lt__(self, other):
        if not isinstance(other, Passenger):
            return NotImplemented
        
        if self.age == -1 or other.age == -1:
            raise ValueError('Cannot compare passengers with unknown')
        
        return self.age < other.age