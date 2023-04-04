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







