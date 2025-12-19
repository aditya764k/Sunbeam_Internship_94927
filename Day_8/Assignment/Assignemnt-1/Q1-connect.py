import mysql.connector

try:
    
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "manager",
        database = "sunbeam_online_portal",
        use_pure = True
    )
    
    if connection.is_connected():
        print("Connection Successful")

except mysql.connector.Error as e:
    print(f"Error connecting to database: {e}")