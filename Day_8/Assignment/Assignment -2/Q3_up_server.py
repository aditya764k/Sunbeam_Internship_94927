from flask import Flask, request , jsonify
from utlis.executeQuery import executeQuery

app = Flask(__name__)

@app.route("/course-u",methods =["PUT"])
def Update_course():
    course_name = request.get_json().get("coursename")
    fees = request.get_json().get("fees")

    query = f"update course set fees = {fees} where course_name = '{course_name}'"
    
    executeQuery(query)

    return jsonify({
        "status": "success",
        "message": f"Course '{course_name}' updated successfully"
    }), 201 

@app.route("/student-u",methods = ["PUT"])
def update_student():
    Mobile_no = request.get_json().get("mobileno")
    name = request.get_json().get("name")

    query = f"update student set Mobile_no = '{Mobile_no}' where name = '{name}'"

    executeQuery(query)

    return jsonify({
        "status": "success",
        "message": f"Student '{name}' Mobile no updated successfully"
    }), 201 


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port = 4000 ,debug = True)