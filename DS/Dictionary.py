# Dictionary in Python is an unordered collection of data values,
# used to store data values like a map, which unlike other Data Types that hold only single value as an element,
#  Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized

# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Output
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# There is also a method called get() that will give you the same result:
# Get the value of the "model" key:
x = thisdict["model"]
x = thisdict.get("model")

# Change Values
# You can change the value of a specific item by referring to its key name:
# Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
# we can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)
# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() function.
# Print the number of items in the dictionary:
print(len(thisdict))


# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
# The del keyword removes the item with the specified key name:
del thisdict["model"]
# The del keyword can also delete the dictionary completely:
del thisdict
# The clear() method empties the dictionary:
thisdict.clear()



# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
#  and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Make a copy of a dictionary with the copy() method:
mydict = thisdict.copy()
# Another way to make a copy is to use the built-in function dict()
mydict = dict(thisdict)


# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)


# values()	Returns a list of all the values in the dictionary
# keys()	Returns a list containing the dictionary's keys
