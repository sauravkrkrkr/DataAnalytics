import numpy as np
import pandas as pd

df = pd.read_csv("../resources/employees.csv")

#Run df.info() — explain it in your own words
#print(df.info())
'''df.info() shows about the name of the columns with their indexing numbers and also the type of data a particular column is holding.
It also shows that how many not-null values are present in a particular column.
If we need to check the number of null values then subtract not-null values from the total number of rows.'''

#loc for 3 columns, rows 10-20
print(df.columns) #If columns name not known, then it will fetch from the file and print the column names.
print(df.loc[10:20, ["Employee_ID","Employee_Name", "Department"]])
'''Output:
   Employee_ID     Employee_Name  Department
10      EMP011      Rekha Chopra       Sales
11      EMP012      Nikhil Sinha          IT
12      EMP013    Kritika Sharma  Operations
13      EMP014       Riya Saxena     Finance
14      EMP015       Dhruv Joshi   Marketing
15      EMP016      Priya Bansal  Operations
16      EMP017       Dhruv Mehta          HR
17      EMP018  Rahul Chatterjee          IT
18      EMP019        Aditi Bose       Sales
19      EMP020     Aniket Kapoor          HR
20      EMP021          Sai Bhat       Sales
'''

#Average Age, Experience & Projects
print(df[["Age", "Experience", "Projects"]].mean())
''' Output:
Age           39.400000
Experience     9.183333
Projects       6.950000
dtype: float64'''

#Try value_counts() on Department
print(df["Department"].value_counts()) #it gives the count of each unique value present in the colunmn.
''' Output:
Department
Marketing     23
Sales         22
Operations    22
Finance       19
IT            19
HR            15
Name: count, dtype: int64
'''