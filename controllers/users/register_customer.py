from models.user import register_customer as regCustomer

def add_customer_controller(db, email, password):
    conn = db.connect()
    user_id = regCustomer.register_customer(conn, email, password)
    db.disconnect(conn)
    return user_id