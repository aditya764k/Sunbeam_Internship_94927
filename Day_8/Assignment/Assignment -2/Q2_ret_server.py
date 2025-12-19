from flask import Flask,request

from utlis.executeSelectQuery import executeSelectQuery

app = Flask(__name__)

@app.route("/course",methods =["GET"])
def retrive_courses():
    query = "select * from course"
    result = executeSelectQuery(query)
    return (result)

@app.route("/student",methods =["GET"])
def retrive_students():
    query = "select * from student"
    result = executeSelectQuery(query)
    return (result)



if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4000, debug = True)