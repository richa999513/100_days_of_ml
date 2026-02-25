# file handling and memory management
file = open("geek.txt", "r")
# Perform file operations
content = file.read()
print(content)

file.close()

f = open("geek.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)

with open("geek.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")

#  exception handling in files
try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()




#  MEMORY MANAGEMENT

#  Garbage Collection - It is a process in which Python automatically frees memory occupied by objects that are no longer in use.
# 1. If an object has no references pointing to it (i.e., nothing is using it), garbage collector removes it from memory.
# 2. This ensures that unused memory can be reused for new objects.

# Reference Counting - It is one of the primary memory management techniques used in Python, where:

# 1. Every object keeps a reference counter, which tells how many variables (or references) are currently pointing to that object.
# 2. When a new reference to the object is created, counter increases.
# 3. When a reference is deleted or goes out of scope, counter decreases.
# 4. If the counter reaches zero, it means no variable is using the object anymore, so Python automatically deallocates (frees) that memory.

a = [1, 2, 3]
b = a

print(id(a), id(b))   # Same ID → both point to same list

b.append(4)
print(a)


#  Memory Optimization with Small Integers - memory interning
# Python applies an internal optimization called object interning for small immutable objects (like integers from -5 to 256 and some strings). Instead of creating a new object every time, Python reuses same object to save memory.

x = 10
y = x
print(id(x),' ',id(y))

# In Python, memory is divided mainly into two parts:

# 1. Stack Memory
# 2. Heap Memory

# Stack Memory - Stack memory is where method/function calls and reference variables are stored.

# 1.Whenever a function is called, Python adds it to the call stack.
# 2.Inside this function, all variables declared (like numbers, strings or temporary references) are stored in stack memory.
# 3.Once the function finishes executing, stack memory used by it is automatically freed.
# 4.In simple terms: Stack memory is temporary and is only alive until the function or method call is running.

# How it Works:
# Allocation happens in a contiguous (continuous) block of memory.
# Python’s compiler handles this automatically, so developers don’t need to manage it.
# It is fast, but it is limited in size and scope (only works within a function call).

# Heap Memory - Heap memory is where actual objects and values are stored.

# 1.When a variable is created, Python allocates its object/value in heap memory.
# 2.Stack memory stores only the reference (pointer) to this object.
# 3.Objects in heap memory can be shared among multiple functions or exist even after a function has finished executing.
# 4.In simple terms: Heap memory is like a storage area where all values/objects live and stack memory just keeps directions (references) to them.

# How it Works:
# Heap memory allocation happens at runtime.
# Unlike stack, it does not follow a strict order it’s more flexible.
# This is where large data structures (lists, dictionaries, objects) are stored.
# Garbage collection is responsible for cleaning up unused objects from heap memory.