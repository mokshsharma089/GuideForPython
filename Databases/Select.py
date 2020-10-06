# Select From a Table
# To select from a table in MySQL, use the "SELECT" statement:
#
# Select all records from the "customers" table, and display the result:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
# We use the fetchall() method, which fetches all rows from the last executed statement.


# Using the fetchone() Method
# If you are only interested in one row, you can use the fetchone() method.
# The fetchone() method will return the first row of the result:
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

# Prevent SQL Injection
# When query values are provided by the user, you should escape the values.
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# The mysql.connector module has methods to escape query values:

# Escape query values by using the placholder %s method:
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
