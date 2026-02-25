# loops functions

for i in range(0,10,2):
    print(i)

li = [1,2,3,4,5,6,7,8,9] # similar for string, dictionary and tuples
for i in li:
    print(i)

dic = {"a":1, "b":2, "c":3}
for i in dic:
    print("%s %d" % (i,dic[i]))
    print(f"{i} {dic[i]}")

j=0
while j <=5:
    print("Hello ML")
    j=j+1

k=0
while k <8:
    k=k+1
    print("Hello python", end='-')
    if k== 3:
        continue
    if k == 5:
        break


print("Hello world",'hello python','hello ML', sep='@')


# function

def odd_even(num):
    if num%2==0:
        print("Even")
    else:
        print("odd")


def myFun(a,b=10): #  Default Arguments
    return a+b


print("Output of myFun() function",myFun(30))
print("Output of myFun() function",myFun(a=30,b=20))#Keyword Arguments

#positonal Arguments-  values are assigned to parameters based on their order in the function call.
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

#Arbitrary Arguments - *args and **kwargs can pass a variable number of arguments to a function

def show(*args,**kwargs):
    print("Non-keyword arguments : \n")
    for arg in args:
        print(arg,sep='-')

    print("keyword arguments : \n")
    for key,value in kwargs.items():
        print(f"{key} : {value}")

show('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')


# nested function
def f1():
    s="i love python"
    def f2():
        print(s)

    f2()

f1()

# anonymous functions- lambda function
cube = lambda x:x**3
print(cube(3))

# variables are references to objects. When we pass them to a function, the behavior depends on whether the object is mutable (like lists, dictionaries) or immutable (like integers, strings, tuples)-pass-by-object-reference

# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified


def factorial(n)->int:
    if n==0:
        return 1
    return n*factorial(n-1)


print(factorial(5))





# Lambda Functions

check = lambda x : "True" if x%2==0 else " False"
print(check(10))

# used with list comprehension
func = [lambda arg=x: arg*10 for x in range(1,6)]
for i in func:
    print(i())

# Calling them later works as intended:
print(func[0]()) # Output: 10
print(func[1]()) # Output: 20
print(func[3]()) # Output: 40

# rreturning multiple values
calc = lambda x, y: (x+y,x*y)
res = calc(3, 4)
print(res)
#Using with filter()-filter() function uses a lambda expression to select elements from a list that satisfy a given condition, such as keeping only even numbers

c = [1, 2, 3, 4, 5, 6]
x = filter(lambda x:x%2==0,c)
print(list(x))

# Using with map()- map() function applies a lambda expression to each element of a list and returns a new list with the transformed values.

c = [1, 2, 3, 4, 5, 6]
x = map(lambda x : x**3,c)
print(list(x)) 

# Using with reduce()-reduce() function repeatedly applies a lambda expression to elements of a list to combine them into a single result.

from functools import reduce
c = [1, 2, 3, 4, 5, 6]
x = reduce(lambda x,y: x+y,c)
print(x)


