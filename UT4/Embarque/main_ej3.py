from pasajero import Passenger
from ferry import Ferry

p1 = Passenger("John", 30)
p2 = Passenger("Mary", 25)
# p3 = Passenger("Peter", -1)
p4 = Passenger("Alice", 47)

# Print the passengers
print(p1)
print(p2)

print('---')

# Ferry
f = Ferry()

# Add the passengers to the ferry
f.add_passenger(p1)
f.add_passenger(p2)

# Add the passengers with the name
f.add_passenger_with_name('Francis')

# Remove the passenger
p_removed = f.remove_passenger()
print(f"The passenger removed:\n{p_removed}")

print('---')

print(f)

print('---')

# Another passenger removed
p_removed = f.remove_passenger()
print(f"The passenger removed:\n{p_removed}")

print('---')

print(f)

print('---')

f.add_passenger(p4)

# The youngest of the ferry (25 years old)
f.add_passenger(p2)

print(f)

print('---')

the_youngest = f.get_youngest()
print(f"The youngest of the ferry is:\n{the_youngest}")