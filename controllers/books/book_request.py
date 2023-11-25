from models.books import book_request as BookRequest

def action_to_book_request_controller(db,borrow_id, status, admin_id):
    conn = db.connect()
    book_id = BookRequest.actionToBookRequest(conn, borrow_id, status, admin_id)
    db.disconnect(conn)
    return book_id