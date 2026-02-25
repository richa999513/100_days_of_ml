# exception handling
# Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
# Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).
try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

# try:
#       # Code 
# except SomeException:
#       # Code 
# else:
#      # Code 
# finally:
#     # Code 

# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.

# Catch-All Handlers and Their Risks - Sometimes we may use a catch-all handler to catch any exception, but it can hide useful debugging info.eg. - ArithmeticError
# x = int("str") -  ValueError
# IndexError - index out of bound
# Criterion - Cause 
# ArithmeticError	
# TypeError	-Operation or function receives an object of an unsupported or incorrect type. eg. - float([5])
# ValueError - Function receives an argument of the correct type, but its value is invalid for the specific operation.eg. - int("abc")

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)


# custom exception
class AgeError(Exception):
    pass

def set(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except AgeError as e:
    print(e)