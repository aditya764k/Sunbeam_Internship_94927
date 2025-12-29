from flask import Blueprint,request,Blueprint
from app.utils.db_utils import executeQuery
from passlib.hash import sha256_crypt as crypto
from app.utils.response import createResult 
from flask_jwt_extended import JWTManager ,jwt_required,get_jwt,get_jwt_identity


user_bp = Blueprint('user',__name__)

@user_bp.route('/register-to-course', methods=['POST'])
def registerToCourse():
   
    required_fields = ['courseId', 'email', 'name', 'mobileNo']

    course_id = request.form.get('courseId')
    email = request.form.get('email')
    name = request.form.get('name')
    mobile_no = request.form.get('mobileNo')
    profile_pic = request.files.get('profile_pic')
    binary_data = None
    if profile_pic:
        binary_data = profile_pic.read()

    query = "SELECT * FROM user WHERE email = %s"
    result = executeQuery(query, (email,))

    if not result:
        default_password = "sunbeam"
        hashed_pw = crypto.hash(default_password)

        user_query = "INSERT INTO user (email, password, role) VALUES (%s, %s, 'Student')"
        executeQuery(user_query, (email, hashed_pw))

    check_reg = "SELECT * FROM student WHERE email = %s AND course_id = %s"
    already_register = executeQuery(check_reg, (email, course_id))

    if already_register:
        return createResult("You are already registered for this course", None)

    registration_query = """
        INSERT INTO student (course_id, email, name, Mobile_no,profile_pic)
        VALUES (%s, %s, %s, %s,%s)
    """
    executeQuery(registration_query, (course_id, email, name, mobile_no,binary_data))

    return createResult(None, "Registration successful, Please Login")

@user_bp.route('/change-password', methods=['PUT'])
@jwt_required() 
def changePassword():
    claims = get_jwt()
    if claims.get("role") != "Student":
            return createResult("Access Denied : Student Only",None)
    
    data = request.get_json()
    required_fileds = ['email', 'newPassword','confirmPassword']
    for field in required_fileds:
        if not data.get(field):
            return createResult("Fill all required fileds",None)
        
    email = data.get('email')
    new_password = data.get('newPassword')
    confirm_password = data.get('confirmPassword')

    if new_password == confirm_password:
        hashed_newpassword = crypto.hash(confirm_password)
        query = "update user set password = %s where email = %s ;"
        params = (hashed_newpassword,email)
        result = executeQuery(query,params)
        
        return createResult(None,"password updated successfully")
    else:
        return createResult("Passwords do not match", None)  

@user_bp.route('/my-courses', methods = ['GET'])
@jwt_required()
def getMyCourses():
    email = get_jwt_identity()
    

    claims = get_jwt()
    if claims.get("role") != "Student":
            return createResult("Access Denied : Student Only",None)

    if not email:
        return createResult("Fill required fields", None)
    
    query = """SELECT s.name, c.*
    FROM course c JOIN student s 
    ON c.course_id = s.course_id 
    WHERE s.email =  %s; """
    params = (email,)
    result = executeQuery(query, params)
    return createResult(None, result)

@user_bp.route('/my-course-with-videos', methods = ['GET'])
@jwt_required()
def getMyCoursesWithVideos():
    email = get_jwt_identity()
    claims = get_jwt()
    if claims.get("role") != "Student":
            return createResult("Access Denied : Student Only",None)
    if not email:
        return createResult("Fill required fields", None)
    
    query = """
    SELECT 
        c.course_id, 
        c.course_name, 
        c.description as course_description,      
        c.fees,             
        c.start_date,       
        c.end_date,         
        c.video_expire_days, 
        v.description as video_description,
        v.video_id, 
        v.title, 
        v.youtube_url, 
        v.added_at
    FROM course c 
    JOIN student s ON c.course_id = s.course_id 
    LEFT JOIN videos v ON c.course_id = v.course_id 
    WHERE s.email = %s;
    """
    params = (email,)
    result = executeQuery(query, params)
    return createResult(None, result)



