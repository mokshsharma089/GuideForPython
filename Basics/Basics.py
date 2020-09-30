import string,random

# print(object(s), sep=separator, end=end, file=file, flush=flush)
# Parameter	Description
# object(s)	Any object, and as many as you like. Will be converted to string before printed
# sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
# end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	Optional. An object with a write method. Default is sys.stdout
# flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

print("ABCDE","XXXXBCDEW",sep="(***)",end="uu")#after end{uu in this case} next line would start immediately
one="moksh"
two="great"
print("{} is {}".format(one,two))#moksh is great
print("{1} is {0}".format(one,two))#great is moksh


print("".join(random.choice(string.ascii_lowercase+string.digits) for _ in range(7)))#works

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'


# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)



# Built-in Data Types
# In programming, data type is an important concept.
#
# Variables can store data of different types, and different types can do different things.
#
# Python has the following data types built-in by default, in these categories:
#
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview


# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
x = list(("apple", "banana", "cherry"))	#makes a list
print(x)
x = tuple(("apple", "banana", "cherry"))#makes a tuple
print(x)


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
print(random.randrange(1, 10))


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# If the python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value “__main__”. If this file is being imported from another module,
#  __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.
if __name__ == "__main__":
    print("Executed when invoked directly")
# if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.


# Python Booleans
# Booleans represent one of two values: True or False
# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
#
# Some Values are False
# In fact, there are not many values that evaluates to False, except empty values,
# such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.



# Python Operators
#
# Arithmetic Operators
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y
#
#
# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# Operator	Description
# is 	        Returns True if both variables are the same object	    {x is y	}
# is not	    Returns True if both variables are not the same object	{x is not y}
#
# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
# Operator	Description	Example
# in 	        Returns True if a sequence with the specified value is present in the object
# not in	    Returns True if a sequence with the specified value is not present in the object
#


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass

# Taking input in Python
# input ( )
# Whatever you enter as input, input function convert it into a string. if you enter an integer value still input() function convert it into a string.
# You need to explicitly convert it into an integer in your code using typecasting.


# Taking multiple inputs from user in Python
# input().split(separator, maxsplit)
x, y = input("Enter a two value: ").split() 
