from cafetera import Cafetera

my_coffee_maker = Cafetera()
my_coffee_maker.fill()

my_coffee_maker.show_status()

# ----------------------------------------------------------

print("> Serving 200 ml of coffee...")

my_coffee_maker.serve(200)
my_coffee_maker.show_status()

# ----------------------------------------------------------

print("> Filling the coffee maker with 500 ml...")

my_coffee_maker.fill_specific_quantity(500)
my_coffee_maker.show_status()

# ----------------------------------------------------------

print("> Emptying the coffee maker...")
my_coffee_maker.empty()
my_coffee_maker.show_status()

# ----------------------------------------------------------

print("> Setting the max capacity to 2000 ml...")
my_coffee_maker.set_max_capacity(2000)
my_coffee_maker.show_status()

# ----------------------------------------------------------

print("> Setting the current capacity to 800 ml...")
my_coffee_maker.set_current_capacity(800)
my_coffee_maker.show_status()

# ----------------------------------------------------------

print("> Error:")
my_coffee_maker.set_current_capacity(-2000) # Error: Current capacity cannot be negative

# ----------------------------------------------------------

print("> Serving 3000 ml of coffee... More than the current capacity")
my_coffee_maker.serve(3000) # Empty the coffee maker; serve the remaining coffee (all in this case)
my_coffee_maker.show_status()