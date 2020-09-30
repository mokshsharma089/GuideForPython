# Square brackets can be used to access elements of the string.
# But we can't delete or update any single character using [] brackets

# Python Program for
# Creation of String

# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
			For
			Life'''
print("\nCreating a multiline String: ")
print(String1)


# Output:
#
# String with the use of Single Quotes:
# Welcome to the Geeks World
#
# String with the use of Double Quotes:
# I'm a Geek
#
# String with the use of Triple Quotes:
# I'm a Geek and I live in a world of "Geeks"
#
# Creating a multiline String:
# Geeks
#             For
#             Life


# String Slicing
# To access a range of characters in the String, method of slicing is used.
# Slicing in a String is done by using a Slicing operator (colon).


# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Example
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])
# -1 means last element && -5 means 5th from last element
# Output
# orl


# String Length
# To get the length of a string, use the len() function.
# Example
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))


# String Methods

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Check String
# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."


# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.
txt = "Company10"
x = txt.isalpha()
print(x)
