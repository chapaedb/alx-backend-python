import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, *params):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        """Establishes the database connection and executes the query."""
        
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
       
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results  # Return the results of the query

    def __exit__(self, exc_type, exc_value, traceback):
        """Closes the database connection, ensuring cleanup."""
        if self.cursor:
            
            self.cursor.close()
        if self.connection:
           
            self.connection.commit()
            self.connection.close()

if __name__ == "__main__":
    db_name = "example.db"

    # Ensure the database and table are initialized
    with ExecuteQuery(db_name, "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)") as _:
        pass
    with ExecuteQuery(db_name, "INSERT INTO users (name, age) VALUES (?, ?)", "Alice", 30) as _:
        pass
    with ExecuteQuery(db_name, "INSERT INTO users (name, age) VALUES (?, ?)", "Bob", 20) as _:
        pass

    # Use the custom context manager to fetch users older than 25
    query = "SELECT * FROM users WHERE age > ?"
    with ExecuteQuery(db_name, query, 25) as results:
        print("Users older than 25:")
        for row in results:
            print(row)
