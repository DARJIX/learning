'''write the python code to print a scattered plot'''
import matplotlib.pyplot as plt
import numpy as np
# Generate some example data
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100) + 5*2
plt.scatter(x, y)
# Customize the plot
plt.title("Scattered Plot")
plt.xlabel('X')
plt.ylabel('Y')
# Show the plot
plt.show()
