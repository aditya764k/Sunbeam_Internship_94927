from flask import Flask, request , jsonify
from utlis.executeQuery import executeQuery

app = Flask(__name__)

#first delete child(student)
@app.route("/studentdel",methods = ["DELETE"])
def Delete_student():
    name = request.get_json().get("name")

    query = f"DELETE FROM student WHERE name = '{name}'"

    executeQuery(query)


    return jsonify({
        "status": "success",
        "message": f"Student '{name}' deleted successfully"
    }), 201 


# delete parent course
@app.route("/coursedel",methods =["DELETE"])
def Delete_course():
    course_name = request.get_json().get("coursename")

    query = f"DELETE FROM course WHERE course_name = '{course_name}'"
    
    executeQuery(query)

    return jsonify({
        "status": "success",
        "message": f"Course '{course_name}' deleted successfully"
    }), 201 



if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port = 4000 ,debug = True)