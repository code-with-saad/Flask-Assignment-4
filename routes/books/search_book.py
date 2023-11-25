from flask import Blueprint, request
from db import db
from controllers.books import search_book as SearchBook
from services.token_service import token_required

search_book_bp = Blueprint("search_book", "user_service")

@search_book_bp.route("/search-book", methods=["GET"])
@token_required
def search_book_route(decoded_data):
    if not request.is_json:
        return {
            "error": {
                "message": "API accept JSON data"
            }
        }, 400
    data = request.get_json()
    books =  SearchBook.search_book_controller(
        db,
        title=data.get("title"),
        description=data.get("description"),
        category_id=data.get("category_id"),
        page=data.get("page"),
    )
    return {
        "data": {
            "books": books
        }
    }, 200
    
    