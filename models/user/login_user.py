def login_user(db_conn, email, password, user_type):
    query = f"""
            SELECT id FROM user WHERE email=(%(email)s) AND password=(%(password)s) AND user_type=(%(user_type)s)
            """
    cur = db_conn.cursor()
    cur.execute(
        query,
        {
            "email": email,
            "password": password,
            "user_type": user_type,
        }
    )
    return cur.fetchone()