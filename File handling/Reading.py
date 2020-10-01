# To open the file, use the built-in open() function.
# The open() function returns a file object,
# which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
# print(f.read())
f.close()

# If the file is located in a different location, you will have to specify the file path, like this:
f= open("/Users/mokshsharma/Desktop/new.txt","r")#works
print(f.read())
f.close()

# Read Only Parts of the File
# By default the read() method returns the whole text,
#  but you can also specify how many characters you want to return:
f= open("/Users/mokshsharma/Desktop/new.txt","r")#open again if have read complete text
print(f.read(2))
f.close()

# Read Lines
# You can return one line by using the readline() method:
# By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)
f.close()
