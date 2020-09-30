# List is a collection which is ordered and changeable. Allows duplicate members.
# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access Items
# You access the list items by referring to the index number:
# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from index 2 to 4.
#Remember that the first item is position 0,
#and note that the item in index 5 is NOT included

# By leaving out the start value, the range will start at the first item:
print(thislist[:4])
# By leaving out the end value, the range will go on to the end of the list:
print(thislist[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
#
# Example
# This example returns the items from index -4 (included) to index -1 (excluded)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Change Item Value
# To change the value of a specific item, refer to the index number:
# Example
# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Loop Through a List
# You can loop through the list items by using a for loop:
# Example
# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# Example
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# List Length
# To determine how many items a list has, use the len() function:
# Example
# Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Add Items
# To add an item to the end of the list, use the append() method:
thislist.append("orange")
# To add an item at the specified index, use the insert() method:
thislist.insert(1, "orange")
# use the extend() method, which purpose is to add elements from one list to another list:
# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
# Note – append() and extend() methods can only add elements at the end.


# Remove Item
# There are several methods to remove items from a list:
# he remove() method removes the specified item:Removes only first occurunce
thislist.remove("banana")
# he pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
# he del keyword removes the specified index:
del thislist[0]
# The del keyword can also delete the list completely:
del thislist
# The clear() method empties the list:
thislist.clear()


# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
#  and changes made in list1 will automatically also be made in list2.
#
# There are ways to make a copy, one way is to use the built-in List method copy().
mylist = thislist.copy()
# Another way to make a copy is to use the built-in method list().
mylist = list(thislist)


# count() Method
# The count() method returns the number of elements with the specified value.
# Return the number of times the value 9 appears int the list:
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)

# reverse() Method
# The reverse() method reverses the order of the elements
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

# sort() Method
# the sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).
# Syntax
# list.sort(reverse=True|False, key=myFunc)
# reverse	 === Optional.      reverse=True will sort the list descending. Default is reverse=False
# key	== Optional.            A function to specify the sorting criteria(s)

# Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)

# Sort the list by the length of the values:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)

# Sort a list of dictionaries based on the "year" value of the dictionaries:
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
