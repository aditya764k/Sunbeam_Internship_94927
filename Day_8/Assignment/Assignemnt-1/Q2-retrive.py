import mysql.connector
   
connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "manager",
        database = "sunbeam_online_portal",
        use_pure = True
)

query1 = "select * from course"
query2 = "select * from student"

cursor = connection.cursor()

cursor.execute(query1)

courses = cursor.fetchall()

print(f"Courses: {courses}")

cursor.execute(query2)

students = cursor.fetchall()

print(f"Students: {students}")

cursor.close()

connection.close()

    
   