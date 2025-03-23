from pasajero import Passenger

# Create a passenger with a negative age
p = Passenger("John", 30)
p2 = Passenger("Mary", 25)

# Compare ages
print(p.__lt__(p2))
print(p2.__lt__(p))