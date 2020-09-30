# The yield statement suspends function’s execution and sends a value back to the caller,
# but retains enough state to enable function to resume where it is left off.
# When resumed, the function continues execution immediately after the last yield run

# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2#2nd time function calls it begins from here
    yield 3#3rd time function calls execution begins from here

# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

# Output
#
# 1
# 2
# 3

# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
	i = 1;

	# An Infinite loop to generate squares
	while True:
		yield i*i
		i += 1 # Next execution resumes
				# from this point

# Driver code to test above generator
# function
for num in nextSquare():
	if num > 100:
		break
	print(num)

# Output:
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100



# Generator-Function
# : A generator-function is defined like a normal function, but whenever it needs to generate a value,
# it does so with the yield keyword rather than return. If the body of a def contains yield,
# the function automatically becomes a generator function

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun():
	print(value)

# Generator-Object : Generator functions return a generator object. Generator objects are used either by
# calling the next method on the generator object or
# using the generator object in a “for in” loop (as shown in the above program).


# A simple generator for Fibonacci Numbers
def fib(limit):
	# Initialize first two Fibonacci Numbers
	a, b = 0, 1
	# One by one yield next Fibonacci Number
	while a < limit:
		yield a
		a, b = b, a + b
# Create a generator object
x = fib(5)
# Iterating over the generator object using next
print(x.__next__()) # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__()) 
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
	print(i)

Output :

0
1
1
2
3

Using for in loop
0
1
1
2
3
