import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# 1. Pandas Series : A Pandas Series is one-dimensional labeled array capable of holding data of any type (integer, string, float, Python objects etc.). The axis labels are collectively called indexes. Series is created by loading the datasets from existing storage

li = [1,2,3,4,5,6]
df = pd.Series(li)
print(df)

# Accessing elements of Series
# Position-based Indexing - In this we use numerical positions similar to lists in Python.
print(df[:3])
# # Label-based Indexing - This method also custom index labels assigned to elements.
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])

print(ser[16])

# indexing and selecting data series
# Indexing could mean selecting all the data some of the data from particular columns. Indexing can also be known as Subset Selection. 
# iloc = for position based selection- The df.iloc indexer is very similar to df.loc but only uses integer locations to make its selections.
print(df.iloc[1:4])
#  loc = label based infexing
print(ser.loc[15:19])

ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])
s_add=ser1.add(ser2)
print(s_add)
s_sub = ser1.sub(ser2)
print(s_sub)
s_mul = ser1.mul(ser2)
print(s_mul)
s_div = ser1.div(ser2)
print(s_div)
s_prod = ser1.prod(axis=0,skipna=True)
print(s_prod)
s_pow = ser1.pow(ser2)
print(s_pow)
s_mean = ser1.mean(axis = 0)
print()
s_cov = ser1.cov(ser2)
print(s_cov)

# # Conversion Operation on Series
ser = pd.Series([1,2,3,4,5])
ser = ser.astype('float')
print(ser)

# prod()	Returns the product of the values for the requested axis
# mean()	Returns the mean of the values for the requested axis
# pow()	    Method is used to put each element of passed series as exponential power of caller series and returned the results
# abs()	    Method is used to get the absolute numeric value of each element in Series/DataFrame
# cov()  	Method is used to find covariance of two series

# --------------------------------------------------------------------------------------

# 2. Pandas DataFrame : Pandas DataFrame is a two-dimensional data structure with labeled axes (rows and columns).

d = load_iris()
df = pd.DataFrame(d.data,columns=d.feature_names)
print(df)

#  creating data frame
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst)
print(type(df))

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df = pd.DataFrame(data)
print(df)

# # selecting, deleting, adding and renaming
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
df = pd.DataFrame(data)
 
print(df[['Name', 'Qualification']])

# selecting column
data = pd.read_csv("nba.csv", index_col ="Name")
first = data.loc["Avery Bradley"]
print(first)
# Operations in Pandas

# Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame.Indexing can also be known as Subset Selection.

# Indexing a Dataframe using indexing operator [] - selecting one or more columns
first = data["Age"]
print(first)

row2 = data.iloc[3] # selection baased on integer location
print(row2)

#  loading the data
df = pd.read_csv("data.csv")
print(df.head())

# Viewing and Exploring Data
print(df.info())

# Handling Missing Data
# to fill null values in a datasets, we use fillna(), replace() and interpolate() 
# isnull(): It returns True for NaN (missing) values and False otherwise.
# notnull(): It returns the opposite, True for non-missing values and False for NaN values.
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

df = pd.DataFrame(dict)
 
print(df.isnull())
print(df.isnull().sum())
df.fillna(0)

# drop missing values - If we want to remove rows or columns with missing data we can use the dropna() method. 
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
df = pd.DataFrame(dict)
print(df.dropna())

bool_series = pd.isnull(df["Fourth Score"])
missing_gender_data = df[bool_series]
print(missing_gender_data) # return rows with missing values in column = Fourth Score
print(df.isna())
nmv = df.notnull()

# # Selecting and Filtering Data
# north_inhabitant = df[df['Region']=='North']
# print(north_inhabitant)

# # adding or removing columns
# df = pd.read_csv('data-.csv')
# df['total'] =df['a']+df['b']
# print(df['total'])

# # grouping data

# res = df.groupby('category')['sales'].sum()
# print(res)

# 1. Iterating Over Rows
# There are several ways to iterate over the rows of a Pandas DataFrame and three common methods are:

# iteritems()
# iterrows()
# itertuples()

dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
df = pd.DataFrame(dict)

for i, j in df.iterrows(): # i= row infex , j = df row Series
    print(i, j)
    print()

# 2. Iterating Over Columns
columns = list(df)
 
for i in columns:
    print (df[i][2])

names = ["Akshit", "Uday", "Sam"]
ages = [25, 30, 35]
cities = ["Gurugram", "New Delhi", "Chicago"]

df = pd.DataFrame({
    "Name": names,
    "Age": ages,
    "City": cities
})

print(df)

# FUNCTION	DESCRIPTION
# index()	Method returns index (row labels) of the DataFrame
# insert()	Method inserts a column into a DataFrame
# add()	Method returns addition of dataframe and other, element-wise (binary operator add)
# sub()	Method returns subtraction of dataframe and other element-wise (binary operator sub)
# mul()	Method returns multiplication of dataframe and other, element-wise (binary operator mul)
# div()	Method returns floating division of dataframe and other element-wise (binary operator truediv)
# unique()	Method extracts the unique values in the dataframe
# nunique()	Method returns count of the unique values in the dataframe
# value_counts()	Method counts the number of times each unique value occurs within the Series
# columns()	Method returns the column labels of the DataFrame
# axes()	Method returns a list representing the axes of the DataFrame
# isnull()	Method creates a Boolean Series for extracting rows with null values
# notnull()	Method creates a Boolean Series for extracting rows with non-null values
# isin()	Method extracts rows from a DataFrame where a column value exists in a predefined collection
# dtypes()	Method returns a Series with the data type of each column. The result’s index is the original DataFrame’s columns
# astype()	Method converts the data types in a Series
# values()	Method returns a Numpy representation of the DataFrame i.e only the values in the DataFrame will be returned, the axes labels will be removed
# sort_values()	Method sorts a data frame in Ascending or Descending order of passed Column
# sort_index()	Method sorts the values in a DataFrame based on their index positions or labels instead of their values but sometimes a data frame is made out of two or more data frames and hence later index can be changed using this method
# loc[]	Method retrieves rows based on index label
# iloc[]	Method retrieves rows based on index position
# ix[]	Method retrieves DataFrame rows based on either index label or index position. This method combines the best features of the .loc[] and .iloc[] methods
# rename()	Method is called on a DataFrame to change the names of the index labels or column names
# drop()	Method is used to delete rows or columns from a DataFrame
# pop()	Method is used to delete rows or columns from a DataFrame
# sample()	Method pulls out a random sample of rows or columns from a DataFrame
# nsmallest()	Method pulls out the rows with the smallest values in a column
# nlargest()	Method pulls out the rows with the largest values in a column
# shape()	Method returns a tuple representing the dimensionality of the DataFrame
# ndim()	Method returns an ‘int’ representing the number of axes / array dimensions.
# Returns 1 if Series, otherwise returns 2 if DataFrame
# dropna()	Method allows the user to analyze and drop Rows/Columns with Null values in different ways
# fillna()	Method manages and let the user replace NaN values with some value of their own
# rank()	Values in a Series can be ranked in order with this method
# query()	Method is an alternate string-based syntax for extracting a subset from a DataFrame
# copy()	Method creates an independent copy of a pandas object
# duplicated()	Method creates a Boolean Series and uses it to extract rows that have duplicate values
# drop_duplicates()	Method is an alternative option to identifying duplicate rows and removing them through filtering
# set_index()	Method sets the DataFrame index (row labels) using one or more existing columns
# reset_index()	Method resets index of a Data Frame. This method sets a list of integer ranging from 0 to length of data as index
# where()	Method is used to check a Data Frame for one or more condition and return the result accordingly. By default, the rows not satisfying the condition are filled with NaN value