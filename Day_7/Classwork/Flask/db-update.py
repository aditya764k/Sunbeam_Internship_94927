# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "student",
    use_pure = True
)

# form a query to be executed
std_name = input("Enter name whose marks to be updated : ")
marks = input("Enter new marks : ")

query = f"update students SET marks = %s where std_name = %s;"
data = (marks, std_name)

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query,data)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()

