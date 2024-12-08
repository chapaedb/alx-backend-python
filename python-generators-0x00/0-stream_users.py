import mysql.connector

def stream_users():
    """
    A generator function to fetch rows one by one from the `user_data` table.

    Yields:
        dict: A dictionary representing a row with keys 'user_id', 'name', 'email', and 'age'.
    """
    try:
        # Establish connection to the database
        connection = mysql.connector.connect(
            host='localhost',  # Update with your MySQL host
            user='root',  # Update with your MySQL username
            password='W7301@jqir#',  # Update with your MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)

        # Execute query to fetch all rows from the user_data table
        cursor.execute("SELECT * FROM user_data")

        # Yield each row one by one
        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Clean up resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()
