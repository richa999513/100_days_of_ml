# Comprehensions in Python

# list comprehensions - Syntax: [expression for item in iterable if condition]
# filtering
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [num for num in a if num % 2 == 0]
print(res)

# Creating a new list
res = [num**2 for num in range(1, 6)]
print(res)

#  Dictionary comprehension
# Syntax:{key_expression: value_expression for item in iterable if condition}
#  creating new dict
dict = {num:num**3 for num in range(6)}

#  mapping 
a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital

res = {state: capital for state, capital in zip(a, b)}
print(res)

# set comprehension
# Syntax:{expression for item in iterable if condition}

res = {num**2 for num in range(1, 6)}
print(res)

# Generator comprehensions-Generator Comprehensions create iterators that generate values lazily, making them memory-efficient as elements are computed only when accessed.

# Syntax: (expression for item in iterable if condition)

res = (num**2 for num in range(1, 6))
print(tuple(res))






# Iterable - A container you can loop over __iter__() or __getitem()

# Iterator - An object that produces elements from an iterable 
# __iter__() - return iterator object, or 
# __next__() - return next element from iterable

