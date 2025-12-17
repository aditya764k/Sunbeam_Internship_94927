import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "student",
    use_pure = True
)

sno = int(input("enter the sno : "))
std_name = input("enter the student name : ")
div = input("enter the class : ")
marks = int(input("enter the marks : "))

# 1. Use %s as placeholders for your variables
query = "INSERT INTO students VALUES (%s, %s, %s, %s)"

# 2. Put your variables into a tuple
data = (sno, std_name, div, marks)

cursor = connection.cursor()

# 3. Pass both the query and the data tuple to execute
cursor.execute(query, data)

connection.commit()
print(f"{cursor.rowcount} record inserted successfully")

cursor.close()
connection.close()