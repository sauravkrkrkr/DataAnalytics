import numpy as np
import pandas as pd

df = pd.read_csv("../resources/employees.csv")

#Run df.info() — explain it in your own words
print(df.info())
'''df.info() shows about the name of the columns with their indexing numbers and also the type of data a particular column is holding.
It also shows that how many not-null values are present in a particular column.
If we need to check the number of null values then subtract not-null values from the total number of rows.'''