# dictionary ,tuples , sets

# DICIONARY
# d = {"richa":21,23:True}
# print(d)
# print(d['richa'])

# d2 = dict(a = "Geeks", b = "for", c = "Geeks")
# print(d2.get('a'))
# # updating existing key
# d[23]=100
# # adding new pair
# d['degree'] = "B.Tech"

# # del: removes an item using its key
# # pop(): removes the item with the given key and returns its value
# # clear(): removes all items from the dictionary
# # popitem(): removes and returns the last inserted key–value pair

# key,value = d.popitem()
# del d[23]
# d.clear()
# v = d2.pop('a')
# print(d2)

# for k in d2:
#     print(k,end='-')

# for key,value in d2.items():
#     print(f'{key} - {value}')

# for v in d2.values():
#     print(v,end='-')



# -----------------------------------------------------
# TUPLE

# t1 = (1,True,'richa',[1,2,3],(1,2))
# print(t1)
# t1[3][0] = 4
# print(t1)
# t2 = tuple([1,2,3,4])
# print(t2)
# t3=tuple("hello")
# print(t3)

# tup1 = (0, 1, 2, 3)
# tup2 = ('python', 'geek')
# tup3 = (tup1, tup2)
# print(tup3)

# tup4 = ('geek',)*3
# print(tup4)

# tup5 = ('geeks')
# m = 5
# for i in range(int(m)):
#     tup5=(tup5,)
#     print(tup5)

# # Accessing Tuple with Indexing
# tup = tuple("Geeks")
# print(tup[0])

# # Accessing a range of elements using slicing
# print(tup[1:4])  
# print(tup[:3])

# # Tuple unpacking
# tup = ("Geeks", "For", "Geeks")

# # This line unpack values of Tuple1
# a, b, c = tup
# print(a)
# print(b)
# print(c)

# # concatinate tuples
# tup1 = (0, 1, 2, 3)
# tup2 = ('Geeks', 'For', 'Geeks')

# tup3 = tup1 + tup2
# print(tup3)



# del tup1

# #  unpacking a tuple
# tup = (1, 2, 3, 4, 5)

# a, *b, c = tup

# print(a) 
# print(b)  # [2, 3, 4]
# print(c)

# -------------------------------------------------------------------
# TUPLE

s = {10, 50, 20}
print(s)
print(type(s))
# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)

# While you cannot modify the individual elements directly, you can still add or remove elements from the set.

my_set = {"apple", "banana", "cherry"}
my_set.remove("banana") # if element NOT found the nexception is raised
my_set.discard("banana") # no exception raised in case of element NOT present
my_set.pop() # The pop() method removes and returns an arbitrary element from the set
print(my_set)

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)

# set based on hash table
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

a.clear()
print(a)


# key in s	containment check
# key not in s	non-containment check
# s1 == s2	s1 is equivalent to s2
# s1 != s2	s1 is not equivalent to s2
# s1 <= s2	s1 is subset of s2
# s1 < s2	s1 is proper subset of s2
# s1 >= s2	s1 is superset of s2
# s1 > s2	s1 is proper superset of s2
# s1 | s2	the union of s1 and s2
# s1 & s2	the intersection of s1 and s2
# s1 - s2	the set of elements in s1 but not s2
# s1 ˆ s2	the set of elements in precisely one of s1 or s2