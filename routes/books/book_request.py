from flask import Blueprint, request
from db import db
from controllers.books import book_request as BookRequest
from services.token_service import token_required

action_to_book_request_bp = Blueprint("action_to_book_request", "user_service")

@action_to_book_request_bp.route("/action-to-book-request", methods=["PUT"])
@token_required
def action_to_book_request_route(decoded_data):
    if (decoded_data["type"] != "ADMIN"):
        return {"error": {"message": "Unauthenticated user"}}, 400
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
    bookId =  BookRequest.action_to_book_request_controller(
        db,
        admin_id=decoded_data["id"],
        borrow_id=data.get("borrow_id"),
        status=data.get("status")
    )
    return {
        "data": {
            "message": "borrow request updated successfully"
        }
    }, 200
    

def validate_data(data):
    error_msg = None
    if data.get("borrow_id") is None or len(str(data.get("borrow_id")).strip()) == 0:
        error_msg = "borrow_id field is required"
    elif data.get("borrow_status") is None or len(data.get("borrow_status").split()) == 0:
        error_msg = "status field is required"
    return error_msg
    