import mysql.connector

def getDBConnection():
    try:
        connection = mysql.connector.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "manager",
            database = "sunbeam_online_portal",
            use_pure = True 
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection = None   

    return connection