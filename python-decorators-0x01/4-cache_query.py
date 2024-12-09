import sqlite3
import functools

# Global cache for query results
query_cache = {}

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

def cache_query(func):
    """
    Decorator to cache query results based on the SQL query string.
    Uses a global dictionary to store results for previously executed queries.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[1] if len(args) > 1 else None)
        if query in query_cache:
            print(f"Using cached result for query: {query}")
            return query_cache[query]
        
        # Execute the query and cache the result
        result = func(*args, **kwargs)
        query_cache[query] = result
        print(f"Cached result for query: {query}")
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """
    Fetch users from the database with caching.
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will execute the query and cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
