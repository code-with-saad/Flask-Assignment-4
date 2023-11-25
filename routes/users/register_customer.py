from flask import Blueprint, request
from db import db
from controllers.users import register_customer as regCustomer

add_customer_bp = Blueprint("add_customer", "user_service")

@add_customer_bp.route("/register-customer", methods=["POST"])
def add_customer_route():
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
    userId =  regCustomer.add_customer_controller(db, email=data.get("email"), password=data.get("password"))
    return {
        "data": {
            "id": userId
        }
    }, 200
    

def validate_data(data):
    error_msg = None
    if data.get("email") is None or len(data.get("email").strip()) == 0:
        error_msg = "email field is required"
    elif data.get("password") is None or len(data.get("password").split()) == 0:
        error_msg = "password field is required"
    return error_msg
    