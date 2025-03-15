from numero import Numero

# Create object
numero1 = Numero()
numero1.set_value(500)
print('Value:', numero1.get_value())
print('Even:', numero1.is_even())
print('Last digit:', numero1.get_last_digit())
print('Add of the digits:', numero1.get_add_digits())

print('-------------------')

numero2 = Numero()
numero2.set_value(456)
print('Value:', numero2.get_value())
print('Is even?', numero2.is_even())
print('Last digit:', numero2.get_last_digit())
print('Add of the digits:', numero2.get_add_digits())

print('-------------------')