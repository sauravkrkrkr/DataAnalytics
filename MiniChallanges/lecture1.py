import numpy as np
import pandas as pd

#Print the dataset shape
rd = pd.read_csv("../resources/employees.csv")
print("Shape of the employee file is :", rd.shape)
#Shape of the employee file is : (120, 10)

#Show the last 8 rows
print("The last 8 rows are: ", rd.tail(8))
''' Output:
The last 8 rows are:      Employee_ID   Employee_Name  Department  Age  Experience  Salary  Performance_Rating  Projects       City Joining_Date
112      EMP113  Rahul Malhotra  Operations   26           3   49000                   4         2  Ahmedabad   2023-09-08
113      EMP114      Saanvi Das   Marketing   24           2   53500                   1         1  Ahmedabad   2024-07-14
114      EMP115  Vishal Rathore  Operations   28           7   57500                   2         6    Lucknow   2019-03-03
115      EMP116    Vikram Ghosh          IT   39          18  111500                   3        10     Jaipur   2015-05-15
116      EMP117   Krishna Reddy   Marketing   49           3   54500                   5         9     Indore   2023-04-14
117      EMP118    Swati Sharma       Sales   36          13   76000                   4        12      Delhi   2015-06-14
118      EMP119   Preeti Kapoor     Finance   38          11   77000                   2         2      Delhi   2015-02-03
119      EMP120  Abhishek Desai       Sales   28           5   55000                   3         9     Jaipur   2021-06-22
'''

#Employee_Name & City for first 10 rows
print(rd[["Employee_Name", "City"]].head(10)) #1st method
print(rd.loc[0:9, ["Employee_Name", "City"]]) #2nd method
''' Output:
      Employee_Name        City
0        Diya Verma      Mumbai
1  Kritika Malhotra      Jaipur
2       Suresh Iyer   Hyderabad
3     Ananya Tiwari     Lucknow
4       Rahul Sinha  Chandigarh
5     Manisha Gupta       Delhi
6      Vihaan Patel     Chennai
7     Vikram Chopra      Jaipur
8     Anushka Verma      Indore
9     Sanjay Tiwari  Chandigarh
'''

#iloc for the employee at row 25
print(rd.iloc[24])
'''Output:
Employee_ID               EMP025
Employee_Name         Amit Singh
Department                 Sales
Age                           57
Experience                    26
Salary                     89500
Performance_Rating             3
Projects                       7
City                     Lucknow
Joining_Date          2015-10-21
Name: 24, dtype: object'''

#Find the maximum Salary
print("The max salary is : ", rd["Salary"].max())
#The max salary is :  127000