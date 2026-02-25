import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# 1. Pandas Series : A Pandas Series is one-dimensional labeled array capable of holding data of any type (integer, string, float, Python objects etc.). The axis labels are collectively called indexes. Series is created by loading the datasets from existing storage

li = [1,2,3,4,5,6]
df = pd.Series(li)
# print(df)

# 2. Pandas DataFrame : Pandas DataFrame is a two-dimensional data structure with labeled axes (rows and columns).

# d = load_iris()
# df = pd.DataFrame(d.data,columns=d.feature_names)
# print(df)

# Operations in Pandas

#  loading the data

df = pd.read_csv("data.csv")
# print(df.head())

# Viewing and Exploring Data

# print(df.info())

# Handling Missing Data

print(df.isnull().sum())
df.fillna(0)

# Selecting and Filtering Data

north_inhabitant = df[df['Region']=='North']
print(north_inhabitant)