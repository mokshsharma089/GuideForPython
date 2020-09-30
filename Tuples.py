# Tuple
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Slicing and access is very similar to lists

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
#
# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Tuples are unchangeable, so you cannot add or remove items from it,
# but you can delete the tuple completely:
#
# The del keyword can delete the tuple completely:
del thistuple

# Join Two Tuples
# To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# Sorted() function
# Sorting any sequence is very easy in Python using built-in method sorted() which does all the hard work for you.
# Sorted() sorts any sequence (list, tuple) and always returns a list with the elements in sorted manner,
# without modifying the original sequence.
