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

# --- STEP 1: Insert into 'course' ---
# course_id is auto_increment, so we skip it
query_course = "INSERT INTO course (course_name, description, fees, start_date, end_date, video_expire_days) VALUES (%s, %s, %s, %s, %s, %s)"
data_course = ("MERN", "Full Stack Web Development", 4000, "2025-12-19", "2026-01-05", 10)

cursor.execute(query_course, data_course)

# Get the auto-generated ID to use for the student
new_course_id = cursor.lastrowid 
print(f"Course inserted. Generated ID: {new_course_id}")

# --- STEP 2: Insert into 'user' ---
# student.email references user.email, so this MUST exist first
query_user = "INSERT INTO user (email, password, role) VALUES (%s, %s, %s)"
data_user = ("aditya_intern@example.com", "pass123", "Student")

cursor.execute(query_user, data_user)
print("User record created.")

# --- STEP 3: Insert into 'student' ---
# reg_no is auto_increment, so we skip it
query_student = "INSERT INTO student (name, email, course_id, Mobile_no, profile_pic) VALUES (%s, %s, %s, %s, %s)"
data_student = ("Aditya", "aditya_intern@example.com", new_course_id, "9876543210", None)

cursor.execute(query_student, data_student)
print("Student record inserted and linked.")

# Save changes and close
connection.commit()
print("\nRecords inserted successfully!")

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