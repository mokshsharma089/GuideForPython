# Try connecting to the database "mydatabase":

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
# If the database does not exist, you will get an error.

Creating a Table

# To create a table in MySQL, use the "CREATE TABLE" statement.
# Make sure you define the name of the database when you create the connection

# Create a table named "customers":
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Primary Key
# When creating a table, you should also create a column with a unique key for each record.
# This can be done by defining a PRIMARY KEY.
# We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1,
# and increased by one for each record.

# Create primary key when creating the table:
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# If the table already exists, use the ALTER TABLE keyword:
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

Insert Into Table
Insert Into Table
To fill a table in MySQL, use the "INSERT INTO" statement.

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Important!: Notice the statement: mydb.commit().
#  It is required to make the changes, otherwise no changes are made to the table.


Insert Multiple Rows
To insert multiple rows into a table, use the executemany() method.
The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# Get Inserted ID
# You can get the id of the row you just inserted by asking the cursor object.
print("1 record inserted, ID:", mycursor.lastrowid)
