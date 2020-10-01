# The OS module in python provides functions for interacting with the operating system
#
# The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents,
#  changing and identifying the current directory, etc.

# os.getcwd():
# Function os.getcwd(),
# returns the Current Working Directory(CWD) of the file used to execute the code, can vary from system to system.
import os
print(os.name)#returns posix
print(os.getcwd())

os.rmdir("new folder")
# Creating Directory
# We can create a new directory using the mkdir() function from the OS module.
os.mkdir("new folder")#creates a new folder with name new file

print(os.getcwd())
# Changing the Current Working Directory
# We must first change the current working directory to a newly created one before doing any operations in it.
#  This is done using the chdir() function.
os.chdir("new folder")#works when given a relative directory name
print(os.getcwd())
os.chdir("/Users/mokshsharma/Desktop/PythonGuideCode")#works when given an absolute path
print(os.getcwd())

# List Files and Sub-directories
# The listdir() function returns the list of all files and directories in the specified directory.
a=os.listdir()#lists files and folders of current working directory
print(a)
a=os.listdir("/Users/mokshsharma/Desktop/PythonGuideCode")#lists files and folders of directory with path mentioned
print(a)
# print(os.getcwd())
# Removing a Directory
# The rmdir() function in the OS module removes the specified directory either with an absolute or relative path.
os.rmdir("new folder")
