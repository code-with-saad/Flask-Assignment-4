from models.user import register_admin as regAdmin

def add_admin_controller(db, email, password):
    conn = db.connect()
    user_id = regAdmin.register_admin(conn, email, password)
    db.disconnect(conn)
    return user_id