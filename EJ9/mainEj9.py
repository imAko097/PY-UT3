from calentador import Calentador

# Create a heater
heater = Calentador(10, 30)

print(heater.get_info())

print('-------------------')

heater.heat()
heater.heat()
heater.heat()

print(heater.get_info())

print('-------------------')

heater.cool()
heater.cool()

print(heater.get_info())