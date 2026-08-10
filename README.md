# DataAnalytics

## Lecture 1

## Why Numpy?
### Numpy stands for numerical python, its a library which allows us to work with numbers especially large list of numbers extremely fast.

### And again before jumping on to VS Code, there is two things uh majorly this is a beginner mistake. they uh usually think of numpy as list because both are defined by box bracket. So they think as in uh list is also a box bracket. Numpai is also box bracket in python. Uh so here is something most beginner don't realize. A normal python list is flexible but that flexibility comes with a cost. It's slow for heavy number chunking. This happens because a Python list can hold a mix of different data types. It can hold a number, a string and all all the things like boolean also. So all in the same list, we can define everything in a same list. I can define my name, 1 can define my age, I can define my address, I can define my uh what uh male or female. So male is true. So this type of boolean value I can define in a list. So that makes list a flexible one but it is slow because of that. Why? Because Python need to check the type of each and every item inside that list.

### On the other hand, numpy is an array force everything to be the same data type. Because of that restriction, NumPy can process the entire array using highly optimized low-level code. Make it 10 or 100 times faster than a normal Python list for numerical work.

### Array are a completely different specialized structure buile for speed and mathematical operations. So array nothing but numpy in python and list is that it can hold, it has flexibility so th can hokd multiple or different types of data types and data in it thats why it is slow.

## What is shape?
### Shape is used to know the number of rows and columns or if we want to know that our data is in 1D or 2D array. 


## Why Pandas?
### Pandas is a library built on top of NumPy, designed to work with structured, table-like data - rows and columns, just like an Excel sheet or a database table, which has more datatypes other than numbers.

### In pandas task like reading a CSV file, filtering rows, handling uh missing values or summarizing a column one line of code task that could take dozen of line in a plain python like this.

### If NumPy is the engine of a car, Pandas is the entire car - steering wheel, dashboard, seats - built using that engine, but designed so a human can drive it comfortably. 
### NumPy handles raw numbers; Pandas handles real-world, labeled, messy data.

## Series and Dataframes in pandas
### SERIES
A single column of data, with an automatic label (an index)
attached to each value.
REAL-WORLD ANALOGY
A Series is like a single column in an Excel sheet - say, just the
"Salary" column — but each row also has a label so you always
know which row you're looking at.
### DATAFRAME
Multiple Series combined side-by-side, forming a full table
with rows and columns. What you'll use 90% of the time.
REAL-WORLD ANALOGY
If a Series is one column of an Excel sheet, a DataFrame is the
entire Excel sheet -every column, every row, all connected together.

## iloc vs loc
### iloc - by Position
Selects rows and columns purely by their numeric position -
like counting seats in a row, regardless of any labels.
Useful for: grabbing "the 3rd record in the file" regardless of label -
e.g. spot-checking a row a colleague mentioned.
### loc - by Label
Selects rows and columns by their label or name - the actual
index or column name, not just position.
Useful for: building focused "mini-reports" - e.g. name and salary
for the first 5 employees - by referencing column names directly.

## Mini-Challanges
### Print the dataset's shape
### Show the last 8 rows
### Employee_Name & City for first 10 rows
### iloc for the employee at row 25
### Find the maximum Salary

## Homework
### Run df.info() — explain it in your own words
### loc for 3 columns, rows 10-20
### Average Age, Experience & Projects
### Try value_counts() on Department



## Lecture 2

## Why Data Cleaning

## isnull() and sum()
### isnull() is used for counting the null enteries in an specific attribute/column. isnull() is a boolean function that will return true for any cell which contains no value
### sum() is used to add up all the null value for a column/attribute.


## Dropna vs Fillna
### Dropna removes rows or columns that contains the missing value. By default it drops any row with even missing values. It can remove rows and columns but by default it removes rows.

### Fillna is used to fill the null cells with intelligent values. Most of the cases we use average value of that particular values's column.

### mean() is the average value.
### mode() is the most frequent value in a column/attribute.
### median() 

## Finding and removing duplicates
### duplicated(), This will check if each column's value in row.
### Each table has primary key, use that primary key to search for the duplicated row. 
### There might be exact duplicate of a row or some columns value are only common.

### subset() and keep()
Subset="Column_name" is used to make a subset of the column which is passed as parameter and keep="first" is used to keep the first occurrence of each duplicate Employee_ID and drop the rest.
If we forget the subset argument then drop_duplicates will ignore the duplicates with space issues, Small&Upper case issue && if we forget about keep , then it will not decide which copy of data we need to keep or remove.

## Renaming Messy Colunms
### Renaming is done with the rename() method with columns attribute.
### Protip: Always trim out the spaces in column names using str.strip() method before renaming because space also has the ascii value which can generatae error if we rename column before striping.

## Unique() method:
### Unique is used to get the unique items in the columns.

## Replace() method:
### This will replace the the words written as keys with the value provided. Like in line no. 72 to 80 of the Lec2.py


## Fitering and Sorting DATA
### Filtering will show only that column that matches the condition. For filter the data we use conditions like df[df["Department"] == "IT"] or df[df["Salary"] > 80000]
### Sorting means to arrange the value in ascending/descending order. For sorting we use sort_values() method with column_name and an attribute named ascending/descending = True/False


## groupby() method
### This will split particular columns in groups, then apply the calculation and then combine into one table.

## Mini-Porject

### Load employees_messy.csv, confirm the mess
### Strip and rename all column header
### Fill missing Salary & Rating (mean / mode)
### Drop rows still missing Age/Experience/City
### Remove duplicates by Employee_ID
### Standardize Department & City text
### Confirm: 120 rows, zero missing values
### Finish with a groupby("Department) sumamry

## Mini-Challanges
### Print how many missing values exist in the City column.
### Strip and rename just the dept column to Department.
### Fill missing Age values with the column's average.
### Filter for Sales employees earning above 60,000.
### Use groupbvll to find the denartment with the hiehest headcount.

## Home-Work
### Fully clean the file and save it as employees_clean_v2.csv.
### Compare its shape to the original Live #1 file - note any differences.
### Find the 3 lowest-rated employees in each department.
### Filter: joined before 2020 AND Performance_Rating ≥ 4 - how many?
### No 3-4 sentences what could cowrong analvzine this data uncleaned?_


## Lecture 5

## Phase 1 - SQL for Analysis

## What is Database?
### An organized digital filing cabinet that stores data - not a messy scattered spreaddsheet.
### Important terms are data, dbms, rdbms
### Install sql workbench 8

### Steps:
CREATE DATABASE company_db;
USE company_db;
CREATE TABLE tablename;

### Sorting and 