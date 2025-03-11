from conversor import Conversor

def main():
    my_converter = Conversor(32)
    print(f"Temperature in Celsius: {round(my_converter.toCelsius(), 2)} C")
    print(f"Temperature in Fahrenheit: {round(my_converter.toFahrenheit(), 2)} F")

main()