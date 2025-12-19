import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "manager",
    database = "student",
    use_pure = True
)

query = "INSERT INTO students VALUES (%s, %s, %s, %s)"

data = [
    (1, 'John', 'A', 85),
    (2, 'Jane', 'B', 90),
    (3, 'Bob', 'A', 78)
]
cursor = connection.cursor()

# Execute multiple statements
cursor.executemany(query, data)


connection.commit()
print("Multiple records inserted successfully")

cursor.close()
connection.close()