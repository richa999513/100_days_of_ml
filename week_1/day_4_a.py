# # collection module - The collections module in Python provides specialized containers

# # Counters - A counter is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents element in the iterable and value represents the count of that element in the iterable.
# from collections import Counter 
  
# # Creating Counter from a list (sequence of items)  
# print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# # Creating Counter from a dictionary
# print(Counter({'A':3, 'B':5, 'C':2}))
  
# # Creating Counter using keyword arguments
# print(Counter(A=3, B=5, C=2))

# # OrderedDict - An OrderedDict is a dictionary that preserves the order in which keys are inserted. While regular dictionaries do this from Python 3.7+, OrderedDict also offers extra features like moving re-inserted keys to the end making it useful for order-sensitive operations.

# from collections import OrderedDict

# print("\nThis is an Ordered Dict:\n") 
# od = OrderedDict() 
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
  
# for key, value in od.items(): 
#     print(key, value)


# # deleting element
# od.pop('a')

# # Re-inserting the same
# od['a'] = 1

# # DefaultDict - A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the key that does not exist and never raises a KeyError.

# # Syntax:class collections.defaultdict(default_factory)

# # default_factory is a function that provides the default value for the dictionary created. If this parameter is absent then the KeyError is raised. value can be - int , bool , str , list , etc.

# from collections import defaultdict # even if element not in dictionary , there will be no error as if key not present , it will be created with a default value
# l = [1,2,6,4,9,7,9,5,3,2,1,0,7,4]
# di = defaultdict(int)
# for i in l:
#     di[i]+=1

# # ChainMap - A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.

# from collections import ChainMap 
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}

# # Defining the chainmap 
# c = ChainMap(d1, d2) 
   
# # Accessing Values using key name
# print(c['a'])

# # Accessing values using values()
# print(c.values())

# # Accessing keys using keys()
# print(c.keys())

# c = c.new_child(d3)


# NamedTuple-A NamedTuple is like a regular tuple but with named fields, making data more readable and accessible. Instead of using indexes, you can access elements by name (e.g., student.fname), which improves code clarity and ease of use.

# Syntax: class collections.namedtuple(typename, field_names)

# from collections import namedtuple
# Student = namedtuple('Student',['name','s_class','roll_no'])
# s = Student("Richa",'12',18)
# print(s[1])
# print(s.name)

# 1. _make(): This function is used to return a namedtuple() from the iterable passed as argument.
# 2. _asdict(): This function returns the OrdereDict() as constructed from the mapped values of namedtuple().

# from collections import namedtuple
  
# # Declaring namedtuple() 
# Student = namedtuple('Student',['name','age','DOB']) 
  
# # Adding values 
# S = Student('Nandini','19','2541997') 
  
# # initializing iterable  
# li = ['Manjeet', '19', '411997' ] 
  
# # using _make() to return namedtuple() 
# print ("The namedtuple instance using iterable is  : ") 
# print (Student._make(li)) 

# # initializing dict 
# di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
  
# # using _asdict() to return an OrderedDict() 
# print ("The OrderedDict instance using namedtuple is  : ") 
# print (S._asdict())


# deque

from collections import deque 
  
# Initializing deque with initial values
de = deque([1, 2, 3]) 
  
# Append 4 to the right end of deque
de.append(4) 
  
# Print deque after appending to the right
print("The deque after appending at right is :") 
print(de) 
  
# Append 6 to the left end of deque
de.appendleft(6) 

# Delete element from the right end (removes 4)
de.pop()

# Print deque after deletion from the right
print("The deque after deleting from right is :") 
print(de)

# Delete element from the left end (removes 6)
de.popleft()

# # UserDict
# # from collections import UserDict 

# # Creating a dictionary where deletion is not allowed
# class MyDict(UserDict): 
      
#     # Prevents using 'del' on dictionary
#     def __del__(self): 
#         raise RuntimeError("Deletion not allowed") 
          
#     # Prevents using pop() on dictionary
#     def pop(self, s=None): 
#         raise RuntimeError("Deletion not allowed") 
          
#     # Prevents using popitem() on dictionary
#     def popitem(self, s=None): 
#         raise RuntimeError("Deletion not allowed") 
      
# # Create an instance of MyDict
# d = MyDict({'a': 1, 'b': 2, 'c': 3})
# d.pop(1) 

# UserList - remove , pop
# UserString - append, remove