# pands-problem-sheet

## Description of the repository
These problems are part of the weekly task of the programming and scripting module.
___

## Index

1. Week 02 - Bank
2. Week 03 - Accounts
3. Week 04 - Collatz
4. Week 05 - Weekday
5. Week 06 . Square root
6. Week 07 - Count_e
7. Week 08 - Plottask
___

### 1. Week 02 - Bank

When Banks are storing currency figures, they store them as integers (usually in cent). 
This is to avoid rounding errors. 
This program adds 2 amounts and converts them from centimos to euros.

* **References:** 

[https://stackoverflow.com/questions/33861401/convert-cents-to-euro]  
In this link there is a discussion about the different ways in which centimos can be converted to euros.

___

### 2. Week 03 - Accounts

Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

This program called accounts.py reads an account number ( with any length) and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).


* **Explanation**
```
final_account = "X" * (len(account_number) - 4) + account_number[-4:]

# The expression "X" * (len(account_number) - 4) creates a string of 'X' characters with a length equal to
# the length of the account number minus the last four digits.
# The last digit of the account number is added using slicing syntax, using the notation [-4:]
# to indicate the last four characters of the account number.
```
* **References:** 

[https://realpython.com/lessons/indexing-and-slicing](https://realpython.com/lessons/indexing-and-slicing/#:~:text=Slicing%20is%20indexing%20syntax%20that,to%20but%20not%20including%20n)
In this link explains a little bit about the slicing syntax.

___

### 3. Week 04 - Collatz


The Collatz Conjecture is a mathematical puzzle that starts with any positive integer. Then enters a loop that continues until "number" equals 1.If it's an even number, divide it by two, but if it's odd, multiply it by three and add one. This process is repeated with the new number obtained, and the goal is to determine if this sequence will eventually reach the number 1.  
This program replicates this conjecture.

* **Explanation**
```
number = int(input("Please enter a positive integer: "))
print(number, end=" ")                # end =" " allows the output numbers to be printed horizontally and separated by spaces 
while number != 1:          
        if number % 2 == 0:                  # Divided by 2 is 0 using the modulus operator (%)
            print((number // 2), end=" ")      
            number = (number // 2)
        elif number % 2 == 1:         
            print((number * 3 + 1), end=" ")
            number = (number * 3) + 1
            
```
* **References:**      
https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff       Collatz Conjecture
https://docs.python.org/3/library/functions.html#print     end =" "  

___

### 4. Week 05 - Weekday

This program indicates whether or not today is a working day, so its output will depend on the day on which the code is tested.

* **Explanation**
```
import datetime     # This module provides classes for working with dates and times
now()               # This method gets the current date(we can use today instead)
weekday()           # This method returns the days as an integer: Monday = 0, Tuesday = 1 ... Sunday = 6
if today < 5:       # Will be True if today is Monday through Friday, since those days have integer values less than 5.
```
* **References:**   
https://docs.python.org/3.3/library/datetime.html#datetime-objects     information about datetime module

___

### 5. Week 06 - Square root










