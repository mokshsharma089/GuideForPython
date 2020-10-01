# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
# os.remove("demofile2.txt")#not sent to trash can but removed forever

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
#
# Check if file exists, then delete it:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

f=open("demofile.txt","w")
f.write("Hey there is some new text here")
f.close()

f=open("demofile.txt","r")
print(f.read())
f.close()

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
  print("Deleted")
else:
  print("The file does not exist")
