# OOPS

class Dog():
    species = 'mammal' # class attribute - All objects of the class share the same value for a class variable unless explicitly overridden in an object.

    def __init__(self, name,age): # constructor
        self.name = name # instance attribute - defined within the __init__ method or other instance methods. Each object maintains its own copy
        self.age = age

# object - state , behavior , identity

d1 = Dog('Tommy', 9)
print(d1.species)
print(d1.name)
# print(d['age']) # TypeError: 'Dog' object is not subscriptable 
d2 = Dog('Barfi', 12)
print(d2.species)
print(d2.name)





