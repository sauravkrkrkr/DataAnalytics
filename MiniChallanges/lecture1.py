import numpy as np
import pandas as pd

#Print the dataset shape
rd = pd.read_csv("../resources/employees.csv")
print("Shape of the employee file is :", rd.shape)

#Show the last 8 rows
print("The last 8 rows are: ", rd.tail(8))

#Employee_Name & City for first 10 rows
print(rd[["Employee_Name", "City"]].head(10)) #1st method
print(rd.loc[0:9, ["Employee_Name", "City"]]) #2nd method

#iloc for the employee at row 25
print(rd.iloc[24])

#Find the maximum Salary
print("The max salary is : ", rd["Salary"].max())