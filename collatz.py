# Asks the user to input any positive integer
# and output successive calculations until the value is 1.
# At each step calculate the next value by following the next rule:
# if it is even, divide it by two.
# if it is odd, multiply it by three and add one.
# Author: Jaime Lara Carrillo

number = int(input("Please enter a positive integer: "))
print(number, end=" ")
while number != 1:
    if number % 2 == 0:
        number = (number // 2)
    else:
        number = (number * 3) + 1
    print(number, end=" ")