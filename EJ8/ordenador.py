class Ordenador:
    # Constructor
    def __init__(self, maxMemory):
        if maxMemory > 0:
            self.maxMemory = maxMemory
        else:
            print('Memory must be greater than 0. Memory set to 1024Mb')
            self.maxMemory = 1024
        
        self.installedMemory = 0
    
    # Get
    def get_max_memoria(self):
        return self.maxMemory
    
    # Get memoria disponible
    def get_memoria_disponible(self):
        return self.maxMemory - self.installedMemory
    
    # Memory empty
    def vaciar_memoria(self):
        self.memoriaInstalada = 0

    # Install 256Mb
    def install_256mb(self):
        if self.installedMemory + 256 > self.maxMemory:
            raise ValueError('Not enough memory')
        else:
            self.installedMemory += 256 
    
    # Install memory
    def install_memory(self, value):
        if self.installedMemory + value > self.maxMemory:
            raise ValueError('Not enough memory')
        else:
            self.installedMemory += value
    
    # Print info
    def print_info(self):
        print('-> Max memory:', self.maxMemory)
        print('-> Memory installed:', self.installedMemory)
        print('-> Memory available:', self.get_memoria_disponible())