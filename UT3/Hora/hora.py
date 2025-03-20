class Hora:
    # Constructor
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    
    # Getter hours
    def get_hours(self):
        return self.hours
    
    # Getter minutes
    def get_minutes(self):
        return self.minutes
    
    # Getter seconds
    def get_seconds(self):
        return self.seconds
    
    # Advance one second
    def one_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
    
    # Show the time
    def show_time(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")