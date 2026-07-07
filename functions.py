#Creating functions
""" A function is defined using the key word def followed by the function name and parentheses.
 The code block within every function starts with a colon (:) and is indented."""
 
def my_function():
    print("Hello, World!")
    
    # This creates a function named my_function that prints "Hello, World!" when called.

# The code inside the function must be indented, and the function can be called by using its name followed by parentheses.

# Calling the function
# To call the function, simply use its name followed by parentheses:
my_function()  # This will output: Hello, World!

# You can call the same function multiple times
my_function()  # This will output: Hello, World!
my_function()  # This will output: Hello, World!

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0
print(fahrenheit_to_celsius(32))  # This will output: 0.0
print(fahrenheit_to_celsius(212))  # This will output: 100.0
print(fahrenheit_to_celsius(98.6))  # This will output: 37.0