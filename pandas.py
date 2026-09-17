import numpy as np
import pandas as pd
print(pd.__version__)
# create dataframe 
df=pd.DataFrame([1,2,3],columns=["col_name"])
print(df)
print(type(df))

data={
    "Name":["Tushar","Mohan","Sanjay","Riya"], 
    "Age":[22,23,32,21],
    "salary":[90000,84848,32333,89999]
}
df_1=pd.DataFrame(data)
print(df_1)
print(type(df_1))
# basic  dataframe understanding 
