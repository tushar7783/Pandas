import numpy as np
import pandas as pd

# Display the installed pandas version
print(pd.__version__)

# =====================================================
# CREATING A DATAFRAME FROM A LIST
# =====================================================

# Create a DataFrame with a single column named 'col_name'
df = pd.DataFrame([1, 2, 3], columns=["col_name"])

print(df)

# Check the datatype of df
print(type(df))

# =====================================================
# CREATING A DATAFRAME FROM A DICTIONARY
# =====================================================

data = {
    "Name": ["Tushar", "Mohan", "Sanjay", "Riya"],
    "Age": [22, 23, 32, 21],
    "salary": [90000, 84848, 32333, 89999]
}

# Convert dictionary into DataFrame
df_1 = pd.DataFrame(data)

print(df_1)

# Check the datatype
print(type(df_1))

# =====================================================
# BASIC DATAFRAME UNDERSTANDING
# =====================================================

# Display first 5 rows (default)
print(df_1.head())

# Display last 2 rows and 'n' rows
print(df_1.tail(2))

# Returns (number_of_rows, number_of_columns)
print(df_1.shape)

# Returns all column names
print(df_1.columns)

# =====================================================
# RENAME COLUMN
# =====================================================

# Rename salary column
# NOTE: By default rename() does NOT modify original DataFrame
df_1.rename(columns={'salary': 'Monthly_salary'})

# Original DataFrame remains unchanged
print(df_1)

# To permanently change the column name,
# use inplace=True
df_1.rename(columns={'salary': 'Monthly_salary'}, inplace=True)

print(df_1)

# =====================================================
# ANOTHER WAY TO RENAME
# =====================================================

# rename() returns a new DataFrame
# Store it in another variable
df_change = df_1.rename(
    columns={'Monthly_salary': 'Monthly_Salary'}
)

print(df_change)

# =====================================================
# DATAFRAME INFORMATION
# =====================================================

# Displays:
# - Number of rows and columns
# - Column names
# - Data types
# - Non-null values
# Usually used for quick data inspection
print(df_1.info())

# =====================================================
# STATISTICAL SUMMARY
# =====================================================

# Gives statistical information for numeric columns:
# count -> total values
# mean  -> average
# std   -> standard deviation
# min   -> minimum value
# 25%   -> first quartile
# 50%   -> median
# 75%   -> third quartile
# max   -> maximum value
print(df_1.describe())


