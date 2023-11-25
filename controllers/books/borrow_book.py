from models.books import borrow_book as BorrowBook

def borrow_book_controller(db,  book_id, user_id, from_date, to_date):
    conn = db.connect()
    borrow_id = BorrowBook.borrow_book(conn, book_id, user_id, from_date, to_date)
    db.disconnect(conn)
    return borrow_id