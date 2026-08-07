import pandas as pd

# Load employees_messy.csv, confirm the messy data, and check for null values
df = pd.read_csv("../resources/employees_messy.csv")
#print(df.shape)
#print(df.isnull().sum())

# Strip and rename all column headers
df.columns = df.columns.str.strip()
renamed_columns = {
    "Employee Name": "Employee_Name",
    "dept": "Department",
    "SALARY": "Salary",
    "Performance Rating": "Performance_Rating",
    "Joining_Date": "Joining_Date",
    "projects": "Projects"
}
df = df.rename(columns = renamed_columns)
#print(df.columns)

#Fill missing Salary & Rating (mean / mode)
avg_salary = df["Salary"].mean()
avg_rating = df["Performance_Rating"].mode()[0]
df["Salary"] = df["Salary"].fillna(avg_salary)
df['Performance_Rating'] = df["Performance_Rating"].fillna(avg_rating)
#print(df[["Salary","Performance_Rating"]])

# Drop rows still missing Age/Experience/City
print(df.shape) #output: 126,10
print(df.dropna().shape) # Print shape after dropping NaN values, Output: 114,10

# Remove duplicates by Employee_ID
df  = df.drop_duplicates(subset="Employee_ID", keep="first")
print(df) #Output : 120,10

