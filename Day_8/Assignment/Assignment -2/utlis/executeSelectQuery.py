from utlis.dbConnection import getDBConnection

def executeSelectQuery(query):
    connection = getDBConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result