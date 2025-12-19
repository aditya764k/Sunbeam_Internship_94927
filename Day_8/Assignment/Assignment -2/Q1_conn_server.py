from flask import Flask 

from utlis.dbConnection import getDBConnection

app = Flask(__name__)

connection = getDBConnection()

if connection:
    print("Database connected successfully")
else:
    print("Failed to connect to database")

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 4000 ,debug = True)