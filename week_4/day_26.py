from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd 
iris = load_iris() 


# A dataset consists of:

# Features (X): Input variables that describe the data
# Target (y): The value we want to predict

# To evaluate a model fairly, we split data into:

# Training set: Used to train the model
# Testing set: Used to evaluate how well the model generalizes

# After splitting, we get:

# X_train, y_train -> Training data
# X_test, y_test -> Testing data

X = iris.data 
y = iris.target 
  
feature_names = iris.feature_names 
target_names = iris.target_names 
  
print("Feature names:", feature_names) 
print("Target names:", target_names) 

print("\nType of X is:", type(X)) 

print("\nFirst 5 rows of X:\n", X[:5])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=42)

print("X_train Shape:",  X_train.shape)
print("X_test Shape:", X_test.shape)
print("Y_train Shape:", y_train.shape)
print("Y_test Shape:", y_test.shape)


#  Handling Categorical Data
# 1. Label Encoding: It converts each category into a unique integer
from sklearn.preprocessing import LabelEncoder

categorical_feature = ['cat', 'dog', 'dog', 'cat', 'bird']

encoder = LabelEncoder()

encoded_feature = encoder.fit_transform(categorical_feature)

print("Encoded feature:", encoded_feature)

# 2. One-Hot Encoding: One-Hot Encoding creates separate binary columns for each category.
# Input must be reshaped into a 2D array
# OneHotEncoder(sparse_output=False) generates binary columns

from sklearn.preprocessing import OneHotEncoder
import numpy as np

categorical_feature = ['cat', 'dog', 'dog', 'cat', 'bird']

categorical_feature = np.array(categorical_feature).reshape(-1, 1)

encoder = OneHotEncoder(sparse_output=False)

encoded_feature = encoder.fit_transform(categorical_feature)

print("OneHotEncoded feature:\n", encoded_feature)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

from sklearn import metrics
print("Logistic Regression model accuracy:", metrics.accuracy_score(y_test, y_pred))

