import numpy as np

a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
ad = np.add(a,b)
print(ad)
sub = np.subtract(a,b)
print(sub)
mul = np.multiply(a,b)
print(mul)
div = np.divide(a,b)
print(div)
pow = np.power(a,b)
print(pow)
md = np.mod(a,b)
print(md)


# numpy array broadcasting - adjusts the smaller array to match the larger array's shape by replicating its values along the necessary dimensions to perform arithmetic operations

a = np.array([[1, 2, 3], [4, 5, 6]])
x = 10
print(a + x)

# Broadcasting applies specific rules to find whether two arrays can be aligned for operations or not that are:

# Check Dimensions: Ensure the arrays have the same number of dimensions or expandable dimensions.
# Dimension Padding: If arrays have different numbers of dimensions the smaller array is left-padded with ones.
# Shape Compatibility: Two dimensions are compatible if they are equal or one of them is 1.

a = np.array([2, 4, 6])
b = np.array([[1, 3, 5], [7, 9, 11]])
res = a + b
print(res)

# Broadcasting in Conditional Operations
a = np.array([12, 24, 35, 45, 60, 72])
b = np.array(["Adult", "Minor"])
res = np.where(a > 18, b[0], b[1])
print(res)

m = np.array([[1, 2], [3, 4]])
v = np.array([10, 20])
res = m * v
print(res)

corr = np.array([1.5, -0.5, 2.0])
res =  corr[:, None] # convet row array to column array
print(res) 


#  Normalizing Image Data
# Centers data by subtracting the mean by ensuring features have zero mean.
# Scales data by dividing by the standard deviation by ensuring features have unit variance.
# Improves numerical stability and performance of algorithms like gradient descent.
img = np.array([ [100, 120, 130],
                 [90, 110, 140],
                 [80, 100, 120] ])

m = img.mean(axis=0)
s = img.std(axis=0)
res = (img - m) / s
print(res)

# centering data

data = np.array([ [10, 20],
                  [15, 25],
                  [20, 30] ])

m = data.mean(axis=0)
res = data - m
print(res)