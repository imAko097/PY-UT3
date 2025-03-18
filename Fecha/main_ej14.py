from fecha import Fecha

# Create a Fecha object
date = Fecha(31, 12, 2025)
date.print_date()
print(f"- Leap? {date.is_leap_year()}") # False
print(f"- Days of December: {date.days_in_month()}") # 31
date.print_date_long() # Wednesday, 31 December 2025

# ------- Set a new date -------

date.set_date(5, 2, 2024)
date.print_date() # 29/02/2024
print(f"- Leap? {date.is_leap_year()}") # True
print(f"- Days of September: {date.days_in_month()}") # 29
date.print_date_long() # Monday, 29 February 2024