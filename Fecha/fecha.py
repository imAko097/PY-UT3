from datetime import datetime
import calendar

class Fecha:
    # Constructor
    def __init__(self, day, month, year):
        self.date = datetime(year, month, day)

    # Getter for the date
    def get_date(self):
        return self.date

    # Setter for the date
    def set_date(self, day, month, year):
        self.date = datetime(year, month, day)
    
    # Method to print the date
    def print_date(self):
        print(self.date.strftime("%d/%m/%Y"))
    
    # Leap year method
    def is_leap_year(self):
        return calendar.isleap(self.date.year)
    
    # Method to get the numbers of days in the month
    def days_in_month(self):
        return calendar.monthrange(self.date.year, self.date.month)[1]
    
    # Print the date in a format like: "Friday, 31 December 2025"
    def print_date_long(self):
        print(self.date.strftime("%A, %d %B %Y"))