def search_book(db_conn, title, description, category, page):
    query = "SELECT * FROM books"
    if title is not None or description is not None or category is not None:
        query += " WHERE "
        if title is not None:
            query += f"title LIKE '%{title}%'"
            if description is not None or category is not None:
                query += " AND "
        if description is not None:
            query += f"description LIKE '%{description}%'"
            if category is not None:
                query += " AND "
        if category is not None:
            query += f"category='{category}'"
    if (page != None):
        query += f" LIMIT 10 OFFSET {(page-1)*10}"
    else:
        query += f" LIMIT 10 OFFSET 0"
    cur = db_conn.cursor()
    cur.execute(query)
    return cur.fetchall()