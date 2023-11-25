from flask import Blueprint, request
from db import db
from controllers.books import add_book as AddBook
from services.token_service import token_required

add_book_bp = Blueprint("add_book", "user_service")

@add_book_bp.route("/add-book", methods=["POST"])
@token_required
def add_book_route(decoded_data):
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
    bookId =  AddBook.add_book_controller(
        db,
        title=data.get("title"),
        description=data.get("description"),
        category_id=data.get("category_id"),
    )
    return {
        "data": {
            "id": bookId
        }
    }, 200
    

def validate_data(data):
    error_msg = None
    if data.get("title") is None or len(data.get("title").strip()) == 0:
        error_msg = "title field is required"
    elif data.get("description") is None or len(data.get("description").split()) == 0:
        error_msg = "description field is required"
    elif data.get("category_id") is None or len(str(data.get("category_id")).split()) == 0:
        error_msg = "category_id field is required"
    return error_msg
    