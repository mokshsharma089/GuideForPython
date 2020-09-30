# Set
# A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.

# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Sets are unordered, so you cannot be sure in which order the items will appear.

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.

# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

# Add Items
# To add one item to a set use the add() method.
thisset.add("orange")
# Add multiple items to a set, using the update() method:
# To add more than one item to a set use the update() method.
thisset.update(["orange", "mango", "grapes"])


# Get the Length of a Set
# To determine how many items a set has, use the len() method.
# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:
# If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

# Remove "banana" by using the discard() method:
# If the item to remove does not exist, discard() will NOT raise an error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.
x = thisset.pop()
# The clear() method empties the set:
thisset.clear()
# The del keyword will delete the set completely:
del thisset


# Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another:

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)


difference()	Returns a set containing the difference between two or more sets
intersection()	Returns a set, that is the intersection of two other sets
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
union()	Return a set containing the union of sets
