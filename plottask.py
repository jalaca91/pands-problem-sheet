# This program displays:
# An histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
# A plot of the function  h(x)=x^3 in the range [0, 10]
# Author: Jaime Lara Carrillo

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
