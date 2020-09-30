# Protected
# To accomplish Protected in Python,
# just follow the convention by prefixing the name of the member by a single underscore “_”.
# for eg self._a=32

# Private
# to define a private member prefix the member name with double underscore “__”.
# for eg self.__a=32

# Python program to
# demonstrate protected members


# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ")
		print(self._a)

obj1 = Derived()

obj2 = Base()

# Calling protected member
# Outside class will result in
# AttributeError
print(obj2.a)


# Output-
# Traceback (most recent call last):
#   File "Private And Protected.py", line 38, in <module>
#     print(obj2.a)
# AttributeError: 'Base' object has no attribute 'a'
