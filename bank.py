# Bank.py
# Returns the sum of 2 amounts in cent to euro
# Author: Jaime Lara
amount1 = int(input("Enter amount1 (in cent): "))
amount2 = int(input("Enter amount2 (in cent): "))
total = (amount1 + amount2)
cent_to_euro_conversion = total/100
print(total, "cent are", "€", cent_to_euro_conversion)