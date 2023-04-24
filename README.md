# pands-problem-sheet

## Description of the repository
These problems are part of the weekly task of the programming and scripting module.
___

## Index

1. [Week 02 - Bank](#week-02---bank)
2. [Week 03 - Accounts](#week-03---accounts)
3. [Week 04 - Collatz](#week-04---collatz)
4. [Week 05 - Weekday](#week-05---weekday)
5. [Week 06 - Square root](#week-06---square-root)
6. [Week 07 - week7](#week-07---week7)
7. [Week 08 - Plottask](#week-08---plottask)

___

### Week 02 - Bank

When Banks are storing currency figures, they store them as integers (usually in cent). 
This is to avoid rounding errors. 
This program adds 2 amounts and converts them from centimos to euros.

* **References:** 

[https://stackoverflow.com/questions/33861401/convert-cents-to-euro]  
In this link there is a discussion about the different ways in which centimos can be converted to euros.

___

### Week 03 - Accounts

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

### Week 04 - Collatz


The Collatz Conjecture is a mathematical puzzle that starts with any positive integer. Then enters a loop that continues until "number" equals 1.If it's an even number, divide it by two, but if it's odd, multiply it by three and add one. This process is repeated with the new number obtained, and the goal is to determine if this sequence will eventually reach the number 1.  
This program replicates this conjecture.

* **Explanation**
```                       
number = int(input("Please enter a positive integer: "))
print(number, end=" ")       # end =" " allows the output numbers to be printed horizontally and separated by spaces   
while number != 1:
    if number % 2 == 0:
        number = (number // 2)
    else:
        number = (number * 3) + 1
    print(number, end=" ")
    
```
* **References:**      
https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff       Collatz Conjecture
https://docs.python.org/3/library/functions.html#print     end =" "  
https://www.datacamp.com/tutorial/python-while-loop   While loop tutorial

___

### Week 05 - Weekday

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

### Week 06 - Square root

This program takes a positive floating-point number as input and outputs an approximation of
its square root using a while loop.  

I approached this problem by using the Newton Method. The algorithm for the Newton method is:
1. We assume an initial approximation of half the number( approx =2)
2.Add this approximate root to the orignal number and divide by two approx = (approx + (num / approx)) / 2
3. Repeat step 2 until a precise value is reached.
The output is a float rounded 

* **Explanation**
```
The loop refines the guess until the difference between the guess and the actual square root is less than 0.0001.  

The purpose of the break statement is to exit the while loop early, when the difference between 
the current approximation of the square root and the actual square root is smaller than 0.0001.

```
* **References:**   
https://stackoverflow.com/questions/70793490/how-do-i-calculate-square-root-in-python    information about square roots
https://www.simplilearn.com/tutorials/python-tutorial/break-in-python#:~:text=You%20can%20use%20break%20in,flow%20to%20the%20outer%20loop  Break statement
___

### Week 07 - week7

_In this file we find 2 files, a text file, which is a short text of the writer Jorge Luis Borges and the other is a .py file that contains the code._
a_Dream.txt  
count.py

* **Explanation**
```
Import sys               This module provides access to variables and functions that interact with the Python interpreter.
filename = sys.argv[1]   Assigns the first command-line argument to the variable filename.
count = text.lower().count("e")   This method returns the number of occurrences of the letter "e" in the file(also capital es)

```

* **References:**  

https://python-course.eu/applications-python/sys-module.php  Import sys  

https://www.w3schools.com/python/python_file_handling.asp  Files  

https://www.programiz.com/python-programming/file-operation  Files
___

### Week 08 - Plottask

This program displays the following:
An histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
A plot of the function  h(x)=x^3 in the range [0, 10]

* **Explanation**

For this program,at the beginning we have to choose additional functionalities, such as the creation of graphs.
So in this case, we import two well-know libraries:

1) *Numpy* which is for numerical computation that allows you to work with large, multi-dimensional arrays and matrices
of numerical data. It provides a wide range of mathematical functions to operate on these arrays, making it an
essential tool for scientific computing, data analysis, and machine learning. To find out more https://numpy.org/
```
import numpy as np 
```
For our program we set the np alias for numpy, which is widely used.

2) *Matplotlib* which is is a plotting library for the Python programming language that provides a wide
 variety of high-quality 2D and 3D graphs and plots. More of this in https://matplotlib.org/
 ```
import matplotlib.pyplot as plt
```
In our program we want to import only the module pyplot. 
This module provides a collection of functions that allow you to create a variety of charts, plots, histograms, and other visualizations.
 
The programme code is as follows: 

```
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
norm_data = np.random.normal(loc=5, scale=2, size=1000)
x = np.linspace(0, 10)
y = x ** 3

plt.plot(x, y, linestyle="dashed", color="orange", label="h(x) = x^3")    # Customise the format
plt.hist(norm_data, label="Normal_distribution")

plt.title("Plottask")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left")    # This line adds a legend to the plot in the upper left corner
plt.show()
```  
To explain this code we will do it in parts:  

``
np.random.seed(1)
``  
np.random.seed(1) function sets the random seed to 1, which ensures that the same sequence of 
random numbers will be generated each time the code is run. This is usefull if we want
to create a graphic that does not change.

``
norm_data = np.random.normal(loc=5, scale=2, size=1000)
``
This line generates 1000 random numbers from a normal distribution with a mean of 5 and a 
standard deviation of 2 using the np.random.normal() function from Numpy.  

``
x = np.linspace(0, 10)
``
This line generates an array of 50 evenly spaced numbers between 0 and 10 using the np.linspace() function from Numpy.  

``
y = x ** 3
``
This line generates an array of values by taking the cube of each number in the x array. These values are stored in the "y" variable.  

``
plt.plot(x, y, linestyle="dashed", color="orange", label="h(x) = x^3")
``
This line creates a plot of the x and y arrays using the plt.plot() function from pyplot.
The plot is created with a dashed line style, an orange color, and a label of "h(x) = x^3".
 
``
plt.hist(norm_data, label="Normal_distribution")
`` 
This line creates a histogram of the norm_data variable using the plt.hist() function from pyplot.
The histogram is labeled "Normal_distribution".

```
plt.title("Plottask")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left")    # This line adds a legend to the plot in the upper left corner
plt.show()
```
This entire block of code customize the graphic,adding a legend to the plot in the upper left corner and 
names to the label "x" and "y"

The resulting graph is as follows:

![Figure_Plottask](https://user-images.githubusercontent.com/110190460/234030113-5f850e0f-d9bb-46d3-8cba-1d29e2511fcd.png)

* **References:**  

https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html  numpy.random.normal

https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/   Matplotlib.pyplot.legend() in Python

https://realpython.com/np-linspace-numpy/   np.linspace()












