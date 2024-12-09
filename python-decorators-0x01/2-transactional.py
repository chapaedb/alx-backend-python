import sqlite3
import functools

def with_db_connection(func):
    """
    Decorator to handle database connection automatically.
    Opens a connection, passes it to the function, and closes it afterward.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def transactional(func):
    """
    Decorator to manage database transactions.
    Commits changes if the function executes successfully, otherwise rolls back.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Execute the wrapped function
            result = func(conn, *args, **kwargs)
            # Commit the transaction
            conn.commit()
            return result
        except Exception as e:
            # Rollback on error
            conn.rollback()
            raise e
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Update the email address of a user in the database.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
print("Email updated successfully.")
