# Program that outputs whether or not today is a weekday
# Weekday() returns the days as an integer: Monday = 0, Tuesday = 1 ... Sunday = 6
# Author: Jaime Lara Carrillo

import datetime

today = datetime.datetime.now().weekday()

if today < 5:  # Will be True if today is Monday through Friday, since those days have integer values less than 5
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")