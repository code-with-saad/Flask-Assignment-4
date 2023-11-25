from models.user import login_user as LoginUser

def login_customer_controller(db, email, password, user_type):
    conn = db.connect()
    user_id = LoginUser.login_user(conn, email, password, user_type)
    db.disconnect(conn)
    return user_id