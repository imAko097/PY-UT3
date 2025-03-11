from contador import Contador

def main():
    my_counter = Contador(0)
    my_counter.printContador()

    print("------------------------------------")

    # Increment
    for i in range(10):
        my_counter.increment()
    my_counter.printContador()

    print("------------------------------------")

    # Decrement
    for i in range(5):
        my_counter.decrement()
    my_counter.printContador()

    print("------------------------------------")

    # Reset
    my_counter.reset()
    my_counter.printContador()


main()