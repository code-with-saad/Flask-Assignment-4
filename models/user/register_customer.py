def register_customer(db_con, name, email, password):
    query = """
            INSERT INTO user (email, password, user_type) 
            VALUES (%(name)s, %(email)s, %(password)s, "Customer")
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