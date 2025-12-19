from utlis.dbConnection import getDBConnection

# for create , update , delete query

def executeQuery(query):
    connection = getDBConnection()

    cursor = connection.cursor()

    cursor.execute(query)

    connection.commit()

    cursor.close()

    connection.close()