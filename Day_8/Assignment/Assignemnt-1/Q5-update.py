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

# --- STEP 1: Update 'course' ---
query_course = "update course set fees = %s where course_name = %s"
data_course = (5000, "MERN")

cursor.execute(query_course, data_course)

# --- STEP 2: Update 'student' ---
query_student = "update student set Mobile_no = %s where name = %s"
data_student = ("7620658338", "Aditya")

cursor.execute(query_student, data_student)
print("Student record updated.")
# Save changes and close
connection.commit()
print("\nRecords updated successfully!")

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


cursor.close()
connection.close()