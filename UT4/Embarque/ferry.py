from pasajero import Passenger

# Contains three passengers; three attributes: sit1, sit2, sit3.
class Ferry:
    # Constructor. Initializes the three passengers to None.
    def __init__(self, capacity = 3):
        self.seats = [None] * capacity # Empty seats
        self.number_of_passengers = 0
    
    # Get the number of passengers
    def get_number_of_passengers(self):
        return self.number_of_passengers
    
    # Details of the ferry
    def __str__(self):
        if self.number_of_passengers == 0:
            return "The ferry is empty"
        
        info_ferry = f"Number of passengers: {self.number_of_passengers}.\n"
        info_ferry += "List of passengers:\n"

        passengers_list = [str(passenger) for passenger in self.seats if passenger is not None]
        info_ferry += "\n".join(passengers_list) # Une la lista en líneas separadas

        return info_ferry

    # Add a passenger to the ferry
    def add_passenger(self, passenger):
        if not isinstance(passenger, Passenger):
            raise TypeError("The passenger must be a Passenger")
        
        try:
            empty_seat = self.seats.index(None) # Find the first empty seat
            self.seats[empty_seat] = passenger
            self.number_of_passengers += 1
        except ValueError:
            raise ValueError("The ferry is full")
        
    # Add a passenger to the ferry with the name
    def add_passenger_with_name(self, name):
        if not isinstance(name, str):
            raise TypeError("The name must be a string")

        if None not in self.seats:
            raise ValueError("The ferry is full")
        
        passenger = Passenger(name)
        self.add_passenger(passenger)
    
    # Remove a passenger from the ferry. Return a passenger object
    def remove_passenger(self):
        if self.number_of_passengers == 0:
            raise ValueError("The ferry is empty")
        
        # Save the passenger removed
        passenger_removed = self.seats[0]

        # Remove the passenger from the ferry
        self.seats = self.seats[1:] + [None] # Move all the passengers to the left, the last one is empty
        self.number_of_passengers -= 1

        return passenger_removed

    # Get the younger of two passengers (private method)
    def _the_yourger_of_two(self, one_passenger, another_passenger):
        if one_passenger is None:
            return another_passenger
        
        if another_passenger is None:
            return one_passenger
        
        if one_passenger.get_age() == -1:
            return another_passenger
        
        if another_passenger.get_age() == -1:
            return one_passenger
        
        return one_passenger if one_passenger.get_age() > another_passenger.get_age() else another_passenger
    
    # Get the youngest of the ferry
    def get_youngest(self):
        if self.number_of_passengers == 0:
            return None
        
        youngest_passenger = None
        for passenger in self.seats:
            if passenger is None:
                youngest_passenger = passenger if youngest_passenger is None else self._the_yourger_of_two(youngest_passenger, passenger)

        return youngest_passenger