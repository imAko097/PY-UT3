class Conversor:
    # Constructor
    def __init__(self, temperature):
        self.temperature = temperature

    # Getter
    def getTemperature(self):
        return self.temperature
    
    # Setter
    def setTemperature(self, temperature):
        self.temperature = temperature
    
    # Fahrenheit to Celsius
    def toCelsius(self):
        return (self.temperature - 32) * 5/9
    
    # to Fahrenheit
    def toFahrenheit(self):
        return (self.temperature * 9/5) + 32