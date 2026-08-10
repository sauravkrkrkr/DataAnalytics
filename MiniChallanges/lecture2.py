import numpy as np
import pandas as pd

df = pd.read_csv("../resources/employees_messy.csv")

# Print how many missing values exist in the City column.
#print(df.columns)
#print(df['City '].isnull().sum())

# Strip and rename just the dept column to Department.
df = df.rename(columns={'dept': 'Department'}) 

# Fill missing Age values with the column's average.
#print(df['Age '].isnull().sum())
df['Age '] = df['Age '].fillna(df['Age '].mean(), inplace=True)
#print(df['Age '].isnull().sum())

# Filter for Sales employees earning above 60,000.
sales_above_60k = df[(df['Department']=='Sales') & (df['SALARY']>60000)]
print(sales_above_60k)

# Use groupby to find the department with the highest headcount.
dept_headcount = df.groupby('Department').size()
print(dept_headcount)