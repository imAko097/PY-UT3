class Cafetera:
    # Constructor
    def __init__(self):
        self.max_capacity = 1000
        self.current_capacity = 0
    
    # Max capacity Getter
    def get_max_capacity(self):
        return self.max_capacity

    # Max capacity Setter
    def set_max_capacity(self, max_capacity):
        self.max_capacity = max_capacity
    
    # Current capacity Getter
    def get_current_capacity(self):
        return self.current_capacity
    
    # Current capacity Setter
    def set_current_capacity(self, current_capacity):
        if current_capacity < 0:
            print("Error: Current capacity cannot be negative")
            return
        self.current_capacity = current_capacity
    
    # Fill the coffee maker
    def fill(self):
        self.current_capacity = self.max_capacity
    
    # Serve a coffee
    def serve(self, quantity):
        if self.current_capacity >= quantity:
            self.current_capacity -= quantity
        else:
            self.current_capacity = 0 # Empty the coffee maker; serve the remaining coffee
    
    # Empty the coffee maker
    def empty(self):
        self.current_capacity = 0
    
    # Fill the coffee maker with a specific quantity
    def fill_specific_quantity(self, quantity):
        if self.current_capacity + quantity <= self.max_capacity:
            self.current_capacity += quantity
        else:
            # Fill the coffee maker to its max capacity
            self.current_capacity = self.max_capacity
    
    # Show the current status of the coffee maker
    def show_status(self):
        print(f"Current capacity: {self.current_capacity} ml")
        print(f"Max capacity: {self.max_capacity} ml")