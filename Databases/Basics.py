# MySQL Database
# To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer.
# You can download a free MySQL database at https://www.mysql.com/downloads/.
#
# Install MySQL Driver
# Python needs a MySQL driver to access the MySQL database.
# In this tutorial we will use the driver "MySQL Connector".
# We recommend that you use PIP to install "MySQL Connector".
# PIP is most likely already installed in your Python environment.
# Navigate your command line to the location of PIP, and type the following:
#
# Create Connection
# Start by creating a connection to the database.
# Use the username and password from your MySQL database:
# import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)
# Output-
# <mysql.connector.connection.MySQLConnection object ar 0x016645F0>


# Creating a Database
# To create a database in MySQL, use the "CREATE DATABASE" statement:

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

# If the above code was executed with no errors, you have successfully created a database.
# Check if Database Exists
# You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:

# Return a list of your system's databases:
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
