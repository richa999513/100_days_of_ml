# Duplicates could happen due to:
# Data entry errors: When the same information is recorded more than once by mistake.
# Merging datasets: When combining data from different sources can lead to overlapping of data that can create duplicates.
# Why Duplicates Can Cause Problems?
# Skewed Analysis
# Inaccurate Models: It can cause machine learning models to overfit
# Increased Computational Costs
# Data Redundancy and unnecessary Complexity


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David'],
    'Age': [25, 30, 25, 35, 30, 40],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'San Francisco']
}

df = pd.DataFrame(data)
duplica = df.duplicated()
print(duplica)

#  remove duplicates
 
#  based on a specific column 
df_no_duplicates_columns = df.drop_duplicates(subset=['Name', 'City'])
print(df_no_duplicates_columns)

# 2. Keeping the First or Last Occurrence - by default the first occurance is kept
df_no_duplicates_columns = df.drop_duplicates(keep='last')