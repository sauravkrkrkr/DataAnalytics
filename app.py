#Lecture 1: Introduction to NumPy and Pandas

# First of all, we need to import the necessary libraries and modules that will be used in our application. This includes libraries for data manipulation, visualization, and any other specific tools required for our analytics tasks.
# write command "pip install numpy pandas" to install the libraries.

import numpy as np

import pandas as pd

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

'''salaries = np.array([50000, 60000, 55000, 70000])
new_salaries = salaries * 1.1  # Increase each salary by 10%
print(new_salaries)  # Output: [55000. 66000. 60500. 77000.]

print("Average salary:", salaries.mean())
print("Maximum salary:", salaries.max())
print("Minimum salary:", salaries.min())'''

'''And second is forgetting that operations like dot mean operations 
returns a new value. They don't change the original array unless and until you assign it. 
For example, this is a new value 55200 is a new value generated'''

#PANDAS :-
'''departments = pd.Series(['HR', 'Finance', 'IT', 'Marketing', 'Sales'])
print(departments)
#So the output will generate series with index and values. The index is automatically generated starting from 0.

data = { 
    "Employee_Name": ["Aarav Sharma", "Priya Nair", "Rohan Verma"], 
    "Department": ["IT", "HR", "Sales"], 
    "Salary": [65000, 42000, 51000]
}
df = pd.DataFrame(data) #Dataframe will give error, bcz python is case sensetive.
print(df)'''
#This will generate a DataFrame with three columns: Employee_Name, Department, and Salary. Each row represents an employee's information.

# If the no of values differ in the columns then it will give value error. So we need to make sure that the number of values in each column is the same.

rd = pd.read_csv("resources/employees.csv")
#We dont want to mess up terminal with whole record of the csv file. So we can use head() function to display only first 5 records of the csv file.
#head function is used to display the first five records/rows from the file.
#print(rd.head()) # Display the first few rows of the DataFrame

#print(rd.tail()) # Display the last five rows of the DataFrame
#print(rd.shape) #quickly check the number of rows and columns in the DataFrame

#print(rd.columns) # Display the column names of the DataFrame

#print(rd.info()) # Display information about the DataFrame, including data types and non-null counts
#print(rd.info) # Display whole rows and columns as it is.

#print(rd.describe()) # Display summary statistics for numerical columns in the DataFrame
#print(rd["Salary"].head()) # Display the Salary column of the DataFrame

#print(rd[["Employee_Name", "Salary", "Department"]].head()) # Display specific columns of the DataFrame

# iloc and loc
print(rd.iloc[2])
print(rd.loc[0:4,["Employee_Name", "Salary"]]) # Display specific rows and columns using loc

