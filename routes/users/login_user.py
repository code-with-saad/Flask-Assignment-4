from flask import Blueprint, request
from db import db
from controllers.users import login_user as LoginUser
from services import token_services

login_user_bp = Blueprint("login_user", "user_service")

@login_user_bp.route("/login", methods=["POST"])
def login_user_route():
    if not request.is_json:
        return {
            "error": {
                "message": "API accept JSON data"
            }
        }, 400
    data = request.get_json()
    if (error := validate_data(data)) is not None:
        return {
            "error": {
                "message": error
            }
        }, 400
    userId =  LoginUser.login_customer_controller(
        db, 
        email=data.get("email"), 
        password=data.get("password"), 
        user_type=data.get("user_type")
        )
    if (userId != None):
        return {
            "message": "user login successfully",
            "token": token_services.enrypt(userId["id"], data.get("user_type"))
        }, 200
    else:
        return {
            "error": {
                "message": "Invalid email or password"
            }
        }, 400
    
    

def validate_data(data):
    error_msg = None
    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"
    elif data.get("password") is None or len(data.get("password").split()) == 0:
        error_msg = "password field is required"
    elif data.get("user_type") is None or len(data.get("user_type").split()) == 0:
        error_msg = "user_type field is required"
    return error_msg