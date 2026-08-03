import pandas as pd

df = pd.read_csv("resources/employees_messy.csv")
print(df.shape)
print(df.columns)

print(df.isnull().sum())
'''Output:
Employee_ID           0
 Employee Name        0
dept                  0
Age                   3
Experience            4
SALARY                8
Performance Rating    6
projects              0
City                  5
Joining_Date          0
dtype: int64
'''

df_dropped = df.dropna()
print(df.shape) #output before cleaning
print(df_dropped.shape) #output after cleaning

avg_salary = df["SALARY"].mean()
df["SALARY"] = df["SALARY"].fillna(avg_salary)
print(df.isnull().sum)
'''Output:
Employee_ID   Employee Name    dept  ...  projects  City   Joining_Date
0          False            False  False  ...     False  False         False
1          False            False  False  ...     False  False         False
2          False            False  False  ...     False  False         False
3          False            False  False  ...     False  False         False
4          False            False  False  ...     False  False         False
..           ...              ...    ...  ...       ...    ...           ...
121        False            False  False  ...     False  False         False
122        False            False  False  ...     False  False         False
123        False            False  False  ...     False  False         False
124        False            False  False  ...     False  False         False
125        False            False  False  ...     False  False         False

[126 rows x 10 columns]>
'''

common_rating = df["Performance Rating"].mode()[0]
df["Performance Rating"] = df["Performance Rating"].fillna(common_rating)
print(df.isnull().sum())
'''Output: The value shown in the output is zero for performance rating column'''

print("Exact duplicate rows: ", df.duplicated().sum())
print("Duplicate Employee IDs: ", df["Employee_ID"].duplicated().sum())

df = df.drop_duplicates(subset="Employee_ID", keep="first")
print(df.shape) #output after removing duplicates

df.columns = df.columns.str.strip()
df = df.rename(columns = {
    "Employee Name": "Employee_Name",
    "dept": "Department",
    "Age": "Age",
    "SALARY": "Salary",
    "Performance Rating": "Performance_Rating",
    "projects": "Projects",
    "City": "City"
})
print(df.columns)

df["Department"] = df["Department"].str.strip()
print(df["Department"].unique()) # unique is used to get the unique values in the column. It will give the output in array format.

dept_map = {
    "It": "IT",
    "I.T.": "IT",
    "it": "IT",
    "Ops": "Operations",
    "Hr": "HR",
    "SALES": "Sales",
    "hr": "HR"
}
df["Department"] = df["Department"].replace(dept_map) #this line will replace the values in the Department column based on the mapping provided in dept_map dictionary.
print(df["Department"].unique()) #After replacing the values, we can check the unique values again to see if the changes were successful.
'''Output:
[ 'Operations',       'Sales',          'IT',     'Finance',   'Marketing',
  'operations', 'Operations ',  ' Marketing',          'HR',    ' Finance',
  'Sales ',        'I.T.',       'sales',         ' HR',   'marketing',
  'IT ']
'''

it_employee = df[df["Department"] == "IT"]
print(it_employee.shape)

high_earners = df[df["Salary"] > 80000]
print(high_earners[["Employee_ID", "Department", "Salary"]].head())

top_paid = df.sort_values("Salary", ascending=False)
print(top_paid[["Employee_Name", "Department", "Salary"]].head())

dept_summary = df.groupby("Department")["Salary"].mean().round(1)
print(dept_summary)
