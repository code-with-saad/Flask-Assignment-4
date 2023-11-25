def add_book(db_conn, title, description, category):
    query = """
        INSERT INTO books (title, description, category)
        VALUES (%(title)s, %(description)s, %(category)s)
    """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "title": title,
            "description": description,
            "category_id": category,
        }
    )
    db_conn.commit()
    return cur.lastrowid