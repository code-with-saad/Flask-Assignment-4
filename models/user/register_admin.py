def register_admin(db_con, name, email, password):
    query = """
            INSERT INTO user (name, email, password, user_type) 
            VALUES (%(name)s, %(email)s, %(password)s, "Admin")
        """
    cur = db_con.cursor()
    cur.execute(
        query,
        {   
            "name": name,
            "email": email,
            "password": password,
        }
    )
    db_con.commit()
    return cur.lastrowid