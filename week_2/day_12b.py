# Handling outliers with Pandas

# Outliers can be classified into two types:

# Univariate Outliers: Outliers detected in one feature or variable.
# Multivariate Outliers: Outliers detected based on relationships between two or more features.
# We should Handle Outliers because they can lead to:

# Skewing of results in statistical analysis.
# Mislead machine learning models.
# Reduce model accuracy.
# Cause high error rates.

# # Visualization Techniques

# 1. Box Plot- shows the minimum, first quartile (Q1), median, third quartile (Q3) and maximum values of the dataset
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Age': [22, 25, 28, 24, 23, 29, 150, 27, 26, 22]}
df = pd.DataFrame(data)

# sns.boxplot(x=df['Age'])
# plt.title("Box Plot for Age")
# plt.show()

# 2. Scatter Plot -  visualize the relationship between two variables 
# sns.scatterplot(x=range(len(df['Age'])), y=df['Age'])
# plt.title("Scatter Plot for Age")
# plt.show()

# # Histogram - displays the frequency distribution

# df['Age'].hist(bins=10)
# plt.title("Histogram for Age")
# plt.show()

# # Statistical Methods
# 1. Z-Score Method : Z-Score method calculates how many standard deviations a data point is from the mean. Data points with a Z-score greater than 3 or less than -3 are considered outliers.
# from scipy import stats

# data = {'Age': [22, 25, 28, 24, 23, 29, 150, 27, 26, 22]}
# df = pd.DataFrame(data)

# z = np.abs(stats.zscore(df['Age']))
# print("Z-Score Values:\n", z)

# outliers = df[z > 3]
# print("Outliers:\n", outliers)

# 2. Interquartile Range (IQR) Method - Interquartile Range (IQR) method identifies outliers by measuring the spread between the first quartile (Q1) and third quartile (Q3). Any data point below Q1−1.5∗IQR or above Q3+1.5∗IQRis considered an outlier.
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
print("Outliers: \n",outliers)

# # How to Handle Outliers?

# 1. Removing Outliers - when have no significance in analysis
df_cleaned = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]
print("Cleaned Data:\n", df_cleaned)

#  2. replacing outliers - reduce their impact without losing data.
#  np.where(condition , val_if_condition_true, val_if_condition_false)
df['Age'] = np.where((df['Age'] < lower_bound) | (df['Age'] > upper_bound), df['Age'].median(), df['Age'])
print("Data after Replacing Outliers:\n", df)

# Cappimg outliers - limits the extreme values to predefined upper and lower bounds
df['Age'] = np.clip(df['Age'], lower_bound, upper_bound)
print("Data after Capping Outliers:\n", df)