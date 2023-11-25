def actionToBookRequest(db_conn, borrow_id, status):
    query = """
            UPDATE book_borrow
            SET borrow_status=%(status)s
            WHERE id=%(borrow_id)s
        """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "status": status,
            "borrow_id": borrow_id
        }
    )
    db_conn.commit()
    return cur.lastrowid