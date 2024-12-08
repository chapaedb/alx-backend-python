import mysql.connector
from mysql.connector import Error
import csv
import uuid


def connect_db():
    """Connects to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL server's host
            user='root',       # Replace with your MySQL username
            password='W7301@jqir#'  # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    """Creates the database ALX_prodev if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev checked/created")
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='W7301@jqir#',  # replace with your MySQL password
            port=3306,  # explicitly adding the port
            database='ALX_prodev'  # make sure this is the correct database name
        )
        if connection.is_connected():
            print("Connected to ALX_prodev database")
            return connection
        else:
            print("Failed to connect.")
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


def create_table(connection):
    """Creates the table user_data if it does not exist."""
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(3,0) NOT NULL,
            INDEX (user_id)
        )
        """
        cursor.execute(create_table_query)
        print("Table user_data checked/created")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, data):
    """Inserts data into the user_data table if it does not exist."""
    try:
        cursor = connection.cursor()
        for row in data:
            user_id = str(uuid.uuid4())
            name, email, age = row['name'], row['email'], row['age']

            # Check if email already exists
            cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
            if not cursor.fetchone():
                insert_query = """
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (user_id, name, email, age))
        connection.commit()
        print("Data inserted successfully")
    except Error as e:
        print(f"Error inserting data: {e}")


def load_csv_data(file_path):
    """Loads data from a CSV file."""
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
            print(f"Loaded {len(data)} rows from {file_path}")
            return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return []


if __name__ == "__main__":
    csv_file = 'user_data.csv'

    # Step 1: Connect to MySQL server
    db_connection = connect_db()
    if db_connection:
        # Step 2: Create the database
        create_database(db_connection)
        db_connection.close()

    # Step 3: Connect to the ALX_prodev database
    prodev_connection = connect_to_prodev()
    if prodev_connection:
        # Step 4: Create the user_data table
        create_table(prodev_connection)

        # Step 5: Load data from CSV and insert into table
        user_data = load_csv_data(csv_file)
        if user_data:
            insert_data(prodev_connection, user_data)

        prodev_connection.close()
