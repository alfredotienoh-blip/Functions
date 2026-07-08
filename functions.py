#Creating functions
""" A function is defined using the key word def followed by the function name and parentheses.
 The code block within every function starts with a colon (:) and is indented."""
 
def hello_function():
    print("Hello, World!")
    
    # This creates a function named hello_function that prints "Hello, World!" when called.

# The code inside the function must be indented, and the function can be called by using its name followed by parentheses.

# Calling the function
# To call the function, simply use its name followed by parentheses:
hello_function()  # This will output: Hello, World!

# You can call the same function multiple times
hello_function()  # This will output: Hello, World!
hello_function()  # This will output: Hello, World!

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0
print(fahrenheit_to_celsius(32))  # This will output: 0.0
print(fahrenheit_to_celsius(212))  # This will output: 100.0
print(fahrenheit_to_celsius(98.6))  # This will output: 37.0



#Return values
# Functions can return values using the return statement. The return statement ends the function execution and sends

def Get_greeting():
    return "Hello, welcome to the program!"
message = Get_greeting()
print(message)  # This will output: Hello, welcome to the program!

#You can use the returned value directly

def get_greeting():
    return "Hello, welcome to the program!"
print(get_greeting())  # This will output: Hello, welcome to the program!

#The pass statement
# Function definations cannot be empty. If you need to create a function placeholder without any code, use the pass statement
def placeholder_function():
    pass  # This function does nothing and serves as a placeholder. 

# Python function arguments
# A function with one argument
def my_function(fname):
    print(fname + " Refsnes")
    
my_function("Emil")  # This will output: Emil Refsnes
my_function("Tobias")  # This will output: Tobias Refsnes
my_function("Linus")  # This will output: Linus Refsnes
    
def greet(name):
    print("Hello, " + name + "!")
        
# Call the new function
greet("Alice")  # This will output: Hello, Alice!

#Number of arguments
# A function must be called with the correct number of arguments. If a function expects 2 arguments, then you must call it with exactly 2 arguments
# This function expects 2 arguments and gets 2 arguments
def my_function(Fname, Lname):
    print(Fname + " " + Lname)
    
my_function("Alfred","Owuor")

# Default parameters
# You can also define default values for parameters in a function. If the caller does not provide a value for that parameter, the default value will be used.
def my_function(country = "Kenya"):
    print("I am from " + country)
    
my_function("Uganda")  # This will output: I am from Uganda
my_function()  # This will output: I am from Kenya
my_function("Tanzania")  # This will output: I am from Tanzania
my_function("Rwanda")  # This will output: I am from Rwanda

#Keyword arguments
#You can send arguments with key=value syntax
def my_function(animal, name):
    print("I have a " + animal)
    print("My " + animal + "'s name is " + name)
    
my_function(animal = "dog", name = "Buddy")  # This will output: I have a dog. My dog's name is Buddy.

#This way with key arguments, the order of arguments does not matter

def my_function(animal, name):
    print("I have a " + animal)
    print("My " + animal + "'s name is " + name)
    
my_function(name = "Buddy", animal = "dog")  # This will output: I have a dog. My dog's name is Buddy.


