def book_returned(db_conn, book_id):
    query = f"""
        UPDATE book
        SET book_status='Available'
        WHERE id='{book_id}'
        """
    cur = db_conn.cursor()
    cur.execute(query)
    db_conn.commit()
    cur.lastrowid