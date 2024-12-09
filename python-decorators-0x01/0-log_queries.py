import sqlite3
import functools

def log_queries(func):
    
        def wrapper(*args, **kwargs):
            query = kwargs.get('query') or (args[0] if args else "")
            print(f"Calling {query}")
            return func(*args, **kwargs)
        return wrapper
   


#### decorator to lof SQL queries

 

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")