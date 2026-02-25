## Lists in Python

# a = [1, 2, 3, 4, 5] # List of integers
# b = ['apple', 'banana', 'cherry'] # List of strings
# c = [1, 'hello', 3.14, True] # Mixed data types

# print(a)
# print(b)
# print(c)

# a = list((1, 2, 3, 'apple', 4.5))  
# print(a)

# b = list("GFG")
# print(b)

# a = [2] * 5
# b = [0] * 7

# print(a)
# print(b)

# a = [10, 20, 30, 40, 50]
# print(a[0])    
# print(a[-1])
# print(a[1:4])   # elements from index 1 to 3

# a = []

# a.append(10)  
# print("After append(10):", a)  

# a.insert(0, 5) #0 is idex and 5 is value to be inserted
# print("After insert(0, 5):", a) 

# a.extend([15, 20, 25])  
# print("After extend([15, 20, 25]):", a) 

# a.clear()
# print("After clear():", a)

a = [10, 20, 30, 40, 50]
a[1] = 25 
print(a)

# remove(): Removes the first occurrence of an element
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index

a = [10, 20, 30, 40, 50]

a.remove(30)

print("after removing 30 using remove()",a)

e = a.pop(1)
print("popped element :",e)

del a[1]
print("after deleting element at index 1 using del statement",a)

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])


#  list comprehension
l = [x**2 for x in range(1,6)]
print(l)