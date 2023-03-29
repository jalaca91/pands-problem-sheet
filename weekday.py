# Program that outputs whether or not today is a weekday
# Author: Jaime Lara Carrillo

import datetime

today = datetime.datetime.now().weekday()

if today < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")