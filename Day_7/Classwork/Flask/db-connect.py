import mysql.connector

try:
    connection = mysql.connector.connect(
        host = "127.0.0.1",   
        port = 3306,
        user = "root",
        password = "manager", 
        use_pure = True,
        database = "student"
    )
    if connection.is_connected():
        print("Successfully connected to the database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

query = "select * from students"
cursor = connection.cursor()
cursor.execute(query)
student = cursor.fetchall()
print(f"Students: {student}")
cursor.close()
connection.close()
