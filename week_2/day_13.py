# Correlation matrix  
import numpy as np 
import pandas as pd

# pandas built in function - np.corrcoef()

# x = [215, 325, 185, 332, 406, 522, 412,
#      614, 544, 421, 445, 408],
# y = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 
#      19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
# matrix = np.corrcoef(x, y)
# print(matrix)

# data = {
#     'x': [45, 37, 42, 35, 39],
#     'y': [38, 31, 26, 28, 33],
#     'z': [10, 15, 17, 21, 12]
# }

#  pandas method - df.corr()

# dataframe = pd.DataFrame(data, columns=['x', 'y', 'z'])
# print("Dataframe is : ")
# print(dataframe)
# matrix = dataframe.corr()
# print("Correlation matrix is : ")
# print(matrix)

# 3. Using Matplotlib and Seaborn for Visualization 
import seaborn as sns
import matplotlib.pyplot as plt

# matrix = dataframe.corr()

# plt.figure(figsize=(8,6))
# sns.heatmap(matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
# plt.title("Correlation Heatmap")
# plt.show()


# example 
from sklearn import datasets

dataset = datasets.load_iris()
df = pd.DataFrame(data =dataset.data,columns=dataset.feature_names)
df["target"] = dataset.target

matrix = df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Iris Dataset Correlation Heatmap")
plt.show()