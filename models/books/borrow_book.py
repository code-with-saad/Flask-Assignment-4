def borrow_book(db_conn, book_id, user_id, from_date, to_date):
    query = """
            INSERT INTO book_borrow (user_id, book_id, from_date, to_date)
            VALUES (%(user_id)s, %(book_id)s, %(from_date)s, %(to_date)s)
        """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "user_id": user_id,
            "book_id": book_id,
            "from_date": from_date,
            "to_date": to_date
        }
    )
    booking_id = cur.lastrowid
    query = """
        UPDATE book
        SET status='Not Available'
        WHERE id=%(book_id)s
    """
    cur.execute(query, {"book_id": book_id})
    db_conn.commit()
    return booking_id