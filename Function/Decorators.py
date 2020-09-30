# Decorators in Python
# In Python, functions are the first class objects, which means that –
# Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
# Functions can be defined inside another function and can also be passed as argument to another function.
#
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
# Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
#
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
import time,math

def abc(func):
    def wrapper(*args,**kwargs):
        print("Inside Wrapper function")
        print("This will be performed everytime a function is called and decorater abc is used above it")
        func(*args,**kwargs)
        print("The function call has been finshed")
    return wrapper

"""
@abc
def f1():

    is equivalent to

f1=abc(f1)

"""


@abc
def printMyName(name):
    print("Your Name is {}".format(name))

@abc
def tellTime():
    print("The Time is ",time.time())

printMyName("Moksh Sharma")
tellTime()

# Output
        # Inside Wrapper function
        # This will be performed everytime a function is called and decorater abc is used above it
        # Your Name is Moksh Sharma
        # The function call has been finshed
        # Inside Wrapper function
        # This will be performed everytime a function is called and decorater abc is used above it
        # The Time is  1601378037.4988182
        # The function call has been finshed








# decorator to calculate duration
# taken by any function.
def calculate_time(func):

    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1

# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)

# Output:
        # 3628800
        # Total time taken in :  factorial 2.0061802864074707





# What if a function returns something –
# store whatever the function returns and return before exiting the inner functions

def hello_decorator(func):
	def inner1(*args, **kwargs):

		print("before Execution")

		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")

		# returning the value to the original frame
		return returned_value

	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

# Output
        # before Execution
        # Inside the function
        # after Execution
        # Sum = 3
