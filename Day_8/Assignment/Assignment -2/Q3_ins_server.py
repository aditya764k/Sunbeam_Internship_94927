from flask import Flask, request, jsonify  
from utlis.executeQuery import executeQuery

app = Flask(__name__)

@app.route("/courses", methods=["POST"])
def Insert_courses():
    
    data = request.get_json()
    course_name = data.get("course_name")
    description = data.get("description")
    fees = data.get("fees")
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    video_expire_days = data.get("video_expire_days")

    query = f"Insert into course (course_name, description, fees, start_date, end_date, video_expire_days) VALUES ('{course_name}', '{description}', {fees}, '{start_date}', '{end_date}', {video_expire_days})"

   
    executeQuery(query) 

    return jsonify({
        "status": "success",
        "message": f"Course '{course_name}' inserted successfully"
    }), 201  

@app.route("/student",methods =["POST"])
def insert_student():
    name = request.get_json().get("name")
    email = request.get_json().get("email")
    course_id = request.get_json().get("courseid")
    Mobile_no = request.get_json().get("mobileno")
    profile_pic = request.get_json().get("profilepic")

    query = f"INSERT INTO student (name, email, course_id, Mobile_no, profile_pic) VALUES ('{name}', '{email}',{course_id},'{Mobile_no}', '{profile_pic}')"

    executeQuery(query)

    return jsonify({
        "status" : "sucess",
        "message": f"Student '{name}' Inserted successfully"
    }), 201



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)