class Calentador:
    # Constructor
    def __init__(self, min_temp, max_temp):
        self.temperature = 15
        self.min_temperature = min_temp
        self.max_temperature = max_temp
        self.increment = 5

    # Heat
    def heat(self):
        if self.temperature + self.increment > self.max_temperature:
            raise ValueError('Temperature too high')
        else:
            self.temperature += self.increment
    
    # Cool
    def cool(self):
        if self.temperature - self.increment < self.min_temperature:
            raise ValueError('Temperature too low')
        else:
            self.temperature -= self.increment

    # Get temp
    def get_temperature(self):
        return self.temperature
    
    # Get info
    def get_info(self):
        return f'Temperature: {self.temperature}\nMin temperature: {self.min_temperature}\nMax temperature: {self.max_temperature}'