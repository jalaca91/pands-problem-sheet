# Program that reads in a text file and outputs the number of e's it contains,including both upper and lowercase
# Author : Jaime Lara Carrillo

import sys

filename = sys.argv[1]
with open(filename) as file:
    text = file.read()
count = text.lower().count("e")

print("The file", filename, "has", count, "letter 'e', .") 