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


# =====================================================
# SAVE AND LOAD DATA FROM CSV
# =====================================================

# Export DataFrame to CSV file
# index=False prevents pandas from creating an extra index column
df_1.to_csv('test_data.csv', index=False)

print("Data successfully saved to test_data.csv")

# Read data from CSV file
load_df = pd.read_csv('test_data.csv')

print("\nLoaded DataFrame:")
print(load_df)

# =====================================================
# COLUMN SELECTION
# =====================================================

print("\nSelecting only the Name column:")
print(load_df[['Name']])

print("\nSelecting Name and Monthly_salary columns:")
print(load_df[['Name', 'Monthly_salary']])

# =====================================================
# ROW SELECTION USING LOC
# =====================================================

# loc is label-based indexing
# It is commonly used for:
# 1. Filtering rows using conditions
# 2. Selecting rows and columns by labels

print("\nRecords where Name is Tushar:")
print(load_df.loc[load_df['Name'] == 'Tushar'])

# Multiple conditions using &
# Both conditions must be True

print("\nRecords where Name is Tushar AND Monthly_salary >= 50000:")
print(
    load_df.loc[
        (load_df['Name'] == 'Tushar') &
        (load_df['Monthly_salary'] >= 50000)
    ]
)

# =====================================================
# ROW SELECTION USING ILOC
# =====================================================

# iloc is position-based indexing
# It works using row and column numbers

print("\nFirst row using iloc")
print(load_df.iloc[0])

print("\nFirst two rows using iloc[0:2]:")
print(load_df.iloc[0:2])

print("\nDisplay all rows:")
print(load_df.iloc[:])

# =====================================================
# DIFFERENCE BETWEEN LOC AND ILOC
# =====================================================

print("\nloc[0:2] -> Includes index 2")
print(load_df.loc[0:2])

print("\niloc[0:2] -> Excludes index 2")
print(load_df.iloc[0:2])

# =====================================================
# EXPLANATION
# =====================================================

print("\nDifference between loc and iloc:")
print("loc  -> Uses row/column labels and includes ending index.")
print("iloc -> Uses row/column positions and excludes ending index.")


