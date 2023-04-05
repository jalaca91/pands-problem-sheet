# Reads in a 10 character account number and outputs the account number
# with only the last 4 digits showing (and the first 6 digits replaced with Xs)
# Author: Jaime Lara Carrillo

account_number = input("Enter account number: ")
final_account = "X" * (len(account_number) - 4) + account_number[-4:]
print(final_account)