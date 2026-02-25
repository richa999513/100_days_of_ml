# # iterators and generators

# # An iterator in Python is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries) one element at a time. It follows the iterator protocol, which involves two key methods:

# # __iter__(): Returns the iterator object itself.
# # __next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.
# # Lazy Evaluation, Generator Integration, Stateful Traversal, Uniform Looping, Composable Logic

# s = "GFG"
# it = iter(s)

# print(next(it))
# print(next(it))
# print(next(it))


# # Creating a Custom Iterator - Steps to follow:

# # Define the Class: Start by defining a class that will act as the iterator.
# # Initialize Attributes: In the __init__() method of the class, initialize any required attributes that will be used throughout the iteration process.
# # Implement __iter__(): This method should return the iterator object itself.
# # Implement __next__(): This method should provide the next item in the sequence each time it's called.

# class even_no():
#     def __iter__(self):
#         self.n = 2
#         return self
#     def __next__(self):
#         x = self.n
#         self.n+=2
#         return x
    
# n = even_no()
# it = iter(n)
# print(next(it))
# print(next(it))

# # StopIteration Exception - StopIteration exception is integrated with Python’s iterator protocol.

# try:
#     print(next(it))
# except StopIteration:
#     print("no more element left")

# # An iterable is any object that can return an iterator, while an iterator is the actual object that performs iteration one element at a time.



# GENERATORS
# generator functions use yield to produce a series of results over time. The function pauses its execution after yield, maintaining its state between iterations. it returns generator object

def fun(max):
    cnt = 1
    while cnt<=max:
        yield cnt
        cnt+=1

gen = fun(5)
for n in gen:
    print(n)


def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for val in fun(): 
    print(val)
    
# Memory Efficient ,No List Overhead ,Lazy Evaluation, Support Infinite Sequences, Pipeline Processing
# Generator Expression
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)
