from flask import Blueprint, request
from db import db
from controllers.books import borrow_book as BorrowBook
from services.token_service import token_required

borrow_book_bp = Blueprint("borrow_book", "user_service")

@borrow_book_bp.route("/borrow-book", methods=["POST"])
@token_required
def borrow_book_route(decoded_data):
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
    bookId =  BorrowBook.borrow_book_controller(
        db,
        book_id=data.get("book_id"),
        user_id=decoded_data["id"],
        from_date=data.get("from_date"),
        to_date=data.get("to_date"),
    )
    return {
        "data": {
            "id": bookId
        }
    }, 200
    

def validate_data(data):
    error_msg = None
    if data.get("book_id") is None or len(str(data.get("book_id")).strip()) == 0:
        error_msg = "book_id field is required"
    elif data.get("from_date") is None or len(str(data.get("from_date")).split()) == 0:
        error_msg = "from_date field is required"
    elif data.get("to_date") is None or len(str(data.get("to_date")).split()) == 0:
        error_msg = "to_date field is required"
    return error_msg
    