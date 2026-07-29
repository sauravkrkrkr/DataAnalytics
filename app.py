#Lecture 1: Introduction to NumPy and Pandas

# First of all, we need to import the necessary libraries and modules that will be used in our application. This includes libraries for data manipulation, visualization, and any other specific tools required for our analytics tasks.
# write command "pip install numpy pandas" to install the libraries.

import numpy as np

'''
# If above line is not written then you will get error "nameError"

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

Suppose if we pass any string value in the array then whole value will be converted into string.
We can perform a mathematical operation on an entire array in a single line, no loop required.'''

salaries = np.array([50000, 60000, 55000, 70000])
new_salaries = salaries * 1.1  # Increase each salary by 10%
print(new_salaries)  # Output: [55000. 66000. 60500. 77000.]

print("Average salary:", salaries.mean())
print("Maximum salary:", salaries.max())
print("Minimum salary:", salaries.min())

'''And second is forgetting that operations like dot mean operations 
returns a new value. They don't change the original array unless and until you assign it. 
For example, this is a new value 55200 is a new value generated'''

#PANDAS :-


