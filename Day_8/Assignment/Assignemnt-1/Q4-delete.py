import mysql.connector

# 1. Establish Connection
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="manager",
    database="sunbeam_online_portal",
    use_pure=True
)
cursor = connection.cursor()

# --- STEP 1: Delete 'student' (The Child) ---

query_student = "DELETE FROM student WHERE name = %s"
data_student = ("Aditya",)
cursor.execute(query_student, data_student)
print("Student record deleted.")

# --- STEP 2: Delete 'course' (The Parent) ---
query_course = "DELETE FROM course WHERE course_name = %s"
data_course = ("MERN",) 
cursor.execute(query_course, data_course)
print("Course record deleted.")

query_user = "DELETE FROM user WHERE email = %s"
data_user = ("aditya_intern@example.com",) 
cursor.execute(query_user, data_user)
print("User record deleted.")

connection.commit()
print("\nRecords deleted successfully!")

print("\n--- COURSE TABLE ---")
cursor.execute("SELECT * FROM course")
record1= cursor.fetchall()

for row in record1:
    print(row)

print("\n--- STUDENT TABLE ---")
cursor.execute("SELECT * FROM student")
record2 = cursor.fetchall()
for row in record2:
    print(row)

print("\n--- USER TABLE ---")
cursor.execute("SELECT * FROM user")
record3 = cursor.fetchall()
for row in record3:
    print(row)
cursor.close()
connection.close()