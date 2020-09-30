#STATIC data members
# The Python approach is simple, it doesn’t require a static keyword.
# All variables which are assigned a value in class declaration are class variables.
# And variables which are assigned values inside methods are instance variables.

# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'				 # Class Variable
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"


# Output:
        # cse
        # cse
        # Geek
        # Nerd
        # 1
        # 2
        # cse

Static Member Functions

#
# A static method does not receive an implicit first argument.
# Syntax:
# class C(object):
#     @staticmethod
#     def fun(arg1, arg2, ...):
#         ...
# returns: a static method for function fun.
# A static method is also a method which is bound to the class and not the object of the class.
# A static method can’t access or modify class state.
# It is present in a class because it makes sense for the method to be present in class.

# Python program to demonstrate
# use of class method and static method.

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('mayank', 21)

print person1.age

# print the result
print Person.isAdult(22)

# Output
    # True
