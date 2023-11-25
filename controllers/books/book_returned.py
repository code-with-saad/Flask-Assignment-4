from models.books import book_returned as BookReturned

def mark_book_returned_controller(db,book_id):
    conn = db.connect()
    book_id = BookReturned.book_returned(conn, book_id)
    db.disconnect(conn)
    return book_id