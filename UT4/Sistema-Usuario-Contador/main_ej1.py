from contador import Contador
from usuario import Usuario
from sistema import Sistema

print("> Testing Contador class...")

# Object
contador = Contador(10)
contador2 = Contador(contador)

# Print the value of the counter
contador.printContador()
contador2.printContador()

print("> Testing Usuario class...")

# User
usuario_test = Usuario("test")
for i in range(10):
    usuario_test.access()

# Print the user's statistics
usuario_test.printStatistics()

print("> Testing Sistema class...")

# Sistema
sistema = Sistema()
for i in range(100):
    sistema.simulateAccess()
sistema.printStatistics()