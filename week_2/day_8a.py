import numpy as np

# 1- D array
a = [0,1,2,3,4,5,6]
arr = np.array(a)

print('list in python',a)
print("Numpy Array in python :", arr)
print(type(a))
print(type(arr))


# mulit dimensional array
l1 =[1,2,3,4]
l2 =[2,3,4,5]
l3 =[3,4,5,6]
arr = np.array([l1,l2,l3])
print("multi dimensional array:",arr)

# parameters in numpy array
# 1. Axis: Axis of an array describes the order of the indexing into the array.
# Axis 0 = one dimensional
# Axis 1 = Two dimensional
# Axis 2 = Three dimensional 

# 2. shape
print(arr.shape)

# 3. Rank: Rank of an array is simply the number of axes or dimensions it has. 
# eg rank of arr =[[1,3,3,4],[5,6,7,8]] is 2

# 4. Data type objects (dtype): Data type objects (dtype) is an example of numpy.dtype class= size of an element.
print(arr.dtype)



# Different Ways of Creating Numpy Array

# 1. numpy.array(): Numpy array object in Numpy is called ndarray.Syntax: numpy.array(parameter)
a1 = np.array([1,2,3,4,5,6,7,8,9,0])
print(a1)

# 2. numpy.fromiter(): The fromiter() function create a new one-dimensional array from an iterable object. Syntax: numpy.fromiter(iterable, dtype, count=-1)
s = 'hello'
a2 = np.fromiter(s,dtype='U2')
print(a2)

# 3. numpy.arange(): This is an inbuilt NumPy function that returns evenly spaced values within a given interval.Syntax:  numpy.arange( start , stop, step , dtype=None )
a3 = np.arange(0,10,3)
print(a3)

# 4. numpy.linspace(): This function returns evenly spaced numbers over a specified between two limits. Syntax: numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

a4 = np.linspace(0.0,10.0,50,True)
print(a4)

# 5. numpy.empty(): This function create a new array of given shape and type without initializing value.Syntax: numpy.empty(shape, dtype=float, order='C')

a5 = np.empty([2,4,6],dtype='int32')
print(a5)


# 6. numpy.ones(): This function is used to get a new array of given shape and type filled with ones (1). Syntax: numpy.ones(shape, dtype=None, order='C')

a6 = np.ones([2],dtype='float32',order='F')
print(a6)

# 7. numpy.zeros(): This function is used to get a new array of given shape and type filled with zeros (0). Syntax: numpy.zeros(shape, dtype=None, order='C')

a7 = np.zeros([2],dtype='float32',order='C')
print(a7)