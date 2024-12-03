from mysql.connector import connect

def get_connection():
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="admin",
            database="biblioteca"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None