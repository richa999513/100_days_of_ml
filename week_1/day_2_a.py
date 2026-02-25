#  strings

p = "hello python" 
t = """
this is a 
multi-line string
"""

# print(t)

# s = 'hello world'
# print(s[2]) #l
# print(s[-4]) #o
# print(s[2:5])
# print(s[::-1])
# print(s[0:7:2]) #for 0 to 6 by hopping 2 characters
# print(s[:3])     # from start to index 2
# print(s[3:])

# for c in s:
#     print(c ,end='-')

# # strings are immutable
# s = "geeksforGeeks"
# s = "G" + s[1:]   # create new string
# print(s)
# # del s # delets string

# q = "hello world world"
# s = q.replace("world",'python')
# print(s)
# print(len(s))
# print(s.upper())
# print(s.lower())
s='hello'
print(s.strip())
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
print(s*3)
s = "GeeksforGeeks"
print("Geeks" in s) # True
print("GfG" in s) # false
i =3
print(f"{s} python f-string")
print("{} python format() {}".format(s,i))




# Python provides a rich set of built-in string methods that let you manipulate and analyze text easily. Here’s a structured overview of the most commonly used ones:

# ---

# ## 🔤 Case Conversion
# - `lower()` → Converts all characters to lowercase  
# - `upper()` → Converts all characters to uppercase  
# - `title()` → Converts string to title case (first letter of each word capitalized)  
# - `capitalize()` → Capitalizes the first character  
# - `swapcase()` → Swaps uppercase to lowercase and vice versa  

# ---

# ## 📍 Searching & Finding
# - `find(sub)` → Returns the index of the first occurrence of `sub` (or -1 if not found)  
# - `index(sub)` → Like `find()`, but raises an error if not found  
# - `count(sub)` → Counts occurrences of `sub`  
# - `startswith(prefix)` → Checks if string starts with `prefix`  
# - `endswith(suffix)` → Checks if string ends with `suffix`  

# ---

# ## ✂️ Modification & Formatting
# - `strip()` → Removes whitespace (or specified characters) from both ends  
# - `lstrip()` / `rstrip()` → Removes whitespace from left/right side  
# - `replace(old, new)` → Replaces occurrences of `old` with `new`  
# - `split(sep)` → Splits string into a list by `sep`  
# - `join(iterable)` → Joins elements of an iterable into a string with the current string as separator  
# - `format()` → Formats values into placeholders `{}`  

# ---

# ## ✅ Checking String Properties
# - `isalnum()` → True if all characters are alphanumeric  
# - `isalpha()` → True if all characters are alphabetic  
# - `isdigit()` → True if all characters are digits  
# - `isspace()` → True if all characters are whitespace  
# - `islower()` / `isupper()` → Checks case  
# - `istitle()` → True if string is in title case  

# ---

# ## 🧩 Other Useful Methods
# - `center(width)` → Centers string within given width  
# - `expandtabs(tabsize)` → Replaces tabs with spaces  
# - `encode()` → Encodes string into bytes  
# - `zfill(width)` → Pads string with zeros on the left  

# ---

# 📌 Example:

# ```python
# s = " Hello World "
# print(s.strip())        # "Hello World"
# print(s.lower())        # " hello world "
# print(s.replace("World", "Python"))  # " Hello Python "
# print(s.split())        # ['Hello', 'World']
# ```

# ---

# Would you like me to create a **cheat sheet table** with examples for each method, so you can quickly reference them while coding? 
