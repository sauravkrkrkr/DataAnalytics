# First of all, we need to import the necessary libraries and modules that will be used in our application. This includes libraries for data manipulation, visualization, and any other specific tools required for our analytics tasks.
# write command "pip install numpy pandas" to install the libraries.

import numpy as np

#Creating a simple 1D array
scores = np.array([85, 90, 78, 92, 88])
print(scores)
print(type(scores))  # Output: <class 'numpy.ndarray'>

# A 2D array : 3 students, 2 subjects each
marks = np.array([
    [85, 90], [78, 92], [88, 76]
])
print(marks)

# About Shape
print("Shape", marks.shape)  # Output: (3, 2)
# Here 3 is the number of rows and 2 is the number of columns.
