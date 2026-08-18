import pandas as pd

df = pd.read_csv("../resources/employees_messy.csv")

#Fully clean the file and save it as employees_clean_v2.csv.
df_cleaned = df.dropna();
df_cleaned.to_csv("../resources/employees_clean_v2.csv", index=False)

# Compare its shape to the original Live #1 file - note any differences.
print(df.shape) # Output: (126, 10)
print(df_cleaned.shape) # Output: (114, 10)

# Find the 3 lowest-rated employees in each department.
