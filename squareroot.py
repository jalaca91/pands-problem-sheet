# This program takes a positive floating-point number as input and outputs an approximation of its square root using the Newton Method
# Author: Jaime Lara Carrillo

def sqrt(num):
    approx = num / 2  # We assume an initial approximation of half the number
    while True:
        diff = abs(approx - (num / approx))
        if diff < 0.0001:
            break
        approx = (approx + (num / approx)) / 2
    return approx

num = float(input("Please insert a number: "))
result = sqrt(num)
rounded_result = round(result, 2)
print(f"The square root of {num} is approx. {rounded_result}")