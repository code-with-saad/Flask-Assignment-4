from models.books import add_book as AddBook

def add_book_controller(db, title, description, category_id):
    conn = db.connect()
    book_id = AddBook.add_book(conn, title, description, category_id)
    db.disconnect(conn)
    return book_id