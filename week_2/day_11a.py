# Working with Missing Data in Pandas

# None: A Python object used to represent missing values in object-type arrays.
# NaN: A special floating-point value from NumPy which is recognized by all systems that use IEEE floating-point standards.
import pandas as pd
import numpy as np

# d = {'First Score': [100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score': [np.nan, 40, 80, 98]}
# df = pd.DataFrame(d)

# Checking Missing Values in Pandas

# Using isnull()
# mv = df.isnull() # return boolean matrix
# print(mv)

# Filtering Data Based on Missing Values
# d = pd.read_csv("employees.csv")

# bool_series = pd.isnull(d["Gender"])
# missing_gender_data = d[bool_series]
# print(missing_gender_data)

# data = {'Name': ['Amit', 'Sita', np.nan, 'Raj'],
#         'Age': [25, np.nan, 22, 28]}

# df = pd.DataFrame(data)

# Check for missing values using isna()
# print(df.isna())

# 3. Checking for Non-Missing Values Using notnull()


# nmg = pd.notnull(d["Gender"])
# nmgd= d[nmg]
# print(nmgd)

# Filling Missing Values in Pandas

#  using fillna()
# d = {'First Score': [100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score': [np.nan, 40, 80, 98]}
# df = pd.DataFrame(d)

# df.fillna(0)
# df = df.fillna(method='pad') # forward fill - forward null values filled ith previous not null values
# df = df.fillna(method='bfill') # backward fill - Fill with Next Value
# can also use axis in all these methods
# print(df)
# fill with specific value in specific column
# d = pd.read_csv("employees.csv")
# d["Gender"].fillna('No Gender') # can also use 'inplace = True' inside the method
#  this returns updated gender field . if put inplace = true the nonly i will be able to see the entire updated data frame 
# data = d.replace(to_replace=np.nan, value=-99)
# print(data[10:25])

# interpolate : The interpolate() function fills missing values using interpolation techniques such as the linear method
df = pd.DataFrame({"A": [12, 4, 5, None, 1], 
                   "B": [None, 2, 54, 3, None], 
                   "C": [20, 16, None, 3, 8], 
                   "D": [14, 3, None, None, 6]})  
print(df)
df.interpolate(method ='linear', limit_direction ='forward')
# Syntax: DataFrame.interpolate(method='linear', axis=0, limit=None, inplace=False, limit_direction='forward', limit_area=None, downcast=None, **kwargs) 
# Parameters :
# method : {‘linear’, ‘time’, ‘index’, ‘values’, ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘krogh’, ‘polynomial’, ‘spline’, ‘piecewise_polynomial’, ‘from_derivatives’, ‘pchip’, ‘akima’} 
# axis : 0 fill column-by-column and 1 fill row-by-row. 
# limit : Maximum number of consecutive NaNs to fill. Must be greater than 0. l
# imit_direction : {‘forward’, ‘backward’, ‘both’}, default ‘forward’ 
# limit_area : None (default) no fill restriction. inside Only fill NaNs surrounded by valid values (interpolate). outside Only fill NaNs outside valid values (extrapolate). If limit is specified, consecutive NaNs will be filled in this direction. 
# inplace : Update the NDFrame in place if possible. 
# downcast : Downcast dtypes if possible. 
# kwargs : keyword arguments to pass on to the interpolating function. 

dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}
df = pd.DataFrame(dict)
# drop row with atleast one null value
df.dropna()
# dropping rows with all null values
df.dropna(how='all')
# dropping column with atleast one null value
df.dropna(axis=1)
# 
nd = df.dropna(axis=0, how='any')

