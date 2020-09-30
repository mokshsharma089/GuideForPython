# Some points on Python class:
#
# Classes are created by keyword class.
# Attributes are the variables that belong to class.
# Attributes are always public and can be accessed using dot (.) operator. Eg.: Myclass.Myattribute
#
# An object consists of :
# State : It is represented by attributes of an object. It also reflects the properties of an object.
# Behavior : It is represented by methods of an object. It also reflects the response of an object with other objects.
# Identity : It gives a unique name to an object and enables one object to interact with other objects.



# Destructors are called when an object gets destroyed. In Python, destructors are not needed as much needed in C++
# because Python has a garbage collector that handles memory management automatically.
class Bus:
    # def __init__(self):
    #     self.color="Pink"
    #     self.number="DL-12378"
    def __init__(self,color=None,number=None):
    #this is a constructor
        if color is None:
            self.color="Pink"
        else:
            self.color=color

        if number is None:
            self.number="DL-12378"
        else:
            self.number=number
    # We can't have 2 __init__ methods even if they have different parameters
    def show(self):
        print("Hi, I am a {0} bus and my plate number is {1}".format(self.color,self.number))

    def __del__(self):
    #this is a destructor
        print("Destructor Called for {0} bus with number {1}".format(self.color,self.number))

a = Bus()
b = Bus("Red","MH-9873")
a.show()
b.show()
