from flask import Blueprint,request
from flask_jwt_extended import create_access_token
from passlib.hash import sha256_crypt as crypto
from app.utils.db_utils import executeQuery
from app.utils.response import createResult
import base64

auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    required_fileds = ['email','password']
    for field in required_fileds:
        if not data.get(field):
            return {"error",f"Field '{field} is required and cannot be empty"}

    query = """
        SELECT u.*, s.profile_pic, s.name 
        FROM user u 
        LEFT JOIN student s ON u.email = s.email 
        WHERE u.email = %s
    """
    result = executeQuery(query,(data.get("email"),))
    success = False
    if len(result) > 0 :
         password = data.get("password")
     #     encpassword = result[0]["password"]
         encpassword=crypto.hash(password)
         success = crypto.verify(password,encpassword)
    if not success:
         return createResult("Inavlid email or password",None)
    
    #Profile_pic Logic
    
    user_data = result[0]
    encoded_pic = None

    if user_data.get("profile_pic"):
        # Convert binary BLOB to Base64 string
        encoded_pic = base64.b64encode(user_data["profile_pic"]).decode('utf-8')
    
    # Replace binary data with the string version so JSON can handle it
    user_data["profile_pic"] = encoded_pic

    result[0]["password"] = "****"
    user_role = result[0]["role"]
    jwt = create_access_token(identity = data.get("email"),
                               additional_claims={"role": user_role},
                               expires_delta =False)
    
    result[0]["token"] = jwt
    return createResult(None,result[0])
