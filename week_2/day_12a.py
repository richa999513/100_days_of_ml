# The groupby() function in Pandas is important for data analysis as it allows us to group data by one or more categories and then apply different functions to those groups.

#  splitting data

# Group data by a single key
import pandas as pd
import numpy as np

data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}
df = pd.DataFrame(data1)
print(df)


df.groupby('Name')
print(df.groupby('Name').groups)

# Grouping data with multiple keys 

df.groupby(['Name', 'Qualification'])
print(df.groupby(['Name', 'Qualification']).groups)

#  Grouping data by sorting keys

df.groupby('Name')['Age'].sum() # default it is sorted
df.groupby(['Name'], sort=False)['Age'].sum() # not sorted


# Grouping data with object attributes

df.groupby('Name').groups

#  Iterating through groups

grp = df.groupby('Name')
for name, group in grp:
    print(name)
    print(group)
    print()

# Selecting a group
grp = df.groupby('Name')
grp.get_group('Jai')

# Step 2: Applying Functions to Groups
# 1. Aggregation:
grp1 = df.groupby('Name')
grp1['Age'].aggregate(np.sum)

grp = df.groupby('Name')
grp['Age'].agg([np.sum, np.mean, np.std])

# 2. Transformation - return a result with the same index as the original data.
data2 = pd.DataFrame({'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA'],
        'Score':[23, 34, 35, 45, 47, 50, 52, 53]}) 
grp2 = data2.groupby('Name')
sc = lambda x: (x - x.mean()) / x.std() 
grp2['Age'].transform(sc)

# 3. Filtration: It is a process which is used to discard groups based on a condition.
grp2 = data2.groupby('Name')
grp2.filter(lambda x: len(x) >= 2)

# Step 3: Combining Results

df.groupby('Name').agg({'Age': 'sum'})