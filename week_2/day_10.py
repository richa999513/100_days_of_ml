import pandas as pd

data = {"Name": ["Eve", "Jack", "Charlie", "Henry", "John"],
        "Age": [25, 30, 35, 40, 45],
        "City": ["NY", "LA", "SF", "Houston", "Seattle"]}
df = pd.DataFrame(data)

print(df.head(3))

print()

print(df.tail(2))

print(df.columns)

print(df.dtypes)

print(df.describe()) # provide statistical summaryof the dataset

print(df[["Name", "City"]])

print(df["City"].unique())

print(df[df["Age"] > 30])

print(df[(df["Age"] > 30) & (df["City"] == "SF")])

print(df[(df["Age"] > 30) | (df["City"] == "LA")])

print(df.iloc[0])

print(df.iloc[0,2]) #  = row index, 2 = column index

print(df.iloc[1:3])

df.set_index("Name", inplace=True)

print(df.loc['Alice'])


#  Update: Modifying Data in Pandas

# Updating a Single Value: 
# df.loc[df["Name"]=="Jack",'Age'] = 42 # work when 'Name' is not an index
df['Jack','Age'] = 42
# print(df.columns)
print(df)

#  Updating an Entire Column:
df['City'] = ['Boston', 'Chicago', 'LA', 'Austin', 'Miami']
print(df)

# Deleting a data

# deleting a column
df = df.drop('City',axis=1)
print(df)

#  deleting a row
df = df.drop(2, axis=0) 
print(df)

# Delete Rows Based on Condition:
df = df[df["Age"]!=25]
print(df)

# Delete entire dataset
del df