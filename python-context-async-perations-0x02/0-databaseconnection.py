import sqlite3
class DatabaseConnection:
    """Database Connection class."""

    def __init__(self, db_name):
        """Initialize the class."""
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
     """Enter method."""
     self.connection = sqlite3.connect(self.db_name)
     return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Closes the database connection, ensuring cleanup."""
        if self.connection:
            self.connection.commit() 
            self.connection.close()
if __name__ == "__main__":
    # Create a test database and table (for demonstration purposes)
    db_name = "example.db"
    with DatabaseConnection(db_name) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))

    # Use the custom context manager to perform a query
    with DatabaseConnection(db_name) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)

    
