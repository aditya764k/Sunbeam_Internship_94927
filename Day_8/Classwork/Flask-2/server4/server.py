# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/student')
def create_student():
    # extract data form form
    rollno = request.form.get('rollno')
    name = request.form.get('name')
    email = request.form.get('email')
    course = request.form.get('course')

    # create a query to add student into table
    query = f"insert into students values({rollno}, '{name}', '{email}', '{course}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "student is added successfully"

@server.get('/student')
def retrieve_students():
    # create a select query
    query = "select * from students;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"students : {data}"

@server.put('/student')
def update_student():
    # extract data form form
    name = request.form.get('name')
    email = request.form.get('email')

    # create a query
    query = f"update students SET email = '{email}' where name = '{name}';"

    # execute the query
    executeQuery(query=query)

    return "email is updated successfully"

@server.delete('/student')
def delete_student():
    # extract data form form
    name = request.form.get('name')

    # create a query
    query = f"delete from students where name = '{name}';"

    # execute the query
    executeQuery(query=query)

    return "student is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)