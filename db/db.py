import pymysql


def connect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="admin",
        db='`library_managment_system`',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def disconnect(conn):
  conn.close()

# Driver Code
if __name__ == "__main__":
    connect()