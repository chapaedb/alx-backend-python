# ALX Backend Python - Python Generators

## Project Overview
This project demonstrates the use of Python to create a generator that streams rows from an SQL database one by one. It includes functionalities to set up a MySQL database, create tables, and populate them with data from a CSV file.

## Objectives
- Set up a MySQL database named `ALX_prodev` with a `user_data` table.
- Populate the table with data from a CSV file (`user_data.csv`).
- Implement a generator to stream rows from the database one by one.

## Files
- **`seed.py`**: Contains functions to set up the database, create tables, and insert data from a CSV file.
- **`0-main.py`**: A script to test the functionality implemented in `seed.py`.
- **`user_data.csv`**: Sample data to populate the `user_data` table.

## Functions in `seed.py`

### `connect_db()`
Connects to the MySQL database server.
- Returns: A MySQL connection object.

### `create_database(connection)`
Creates the `ALX_prodev` database if it does not already exist.
- Parameters:
  - `connection`: A MySQL connection object.

### `connect_to_prodev()`
Connects to the `ALX_prodev` database.
- Returns: A MySQL connection object.

### `create_table(connection)`
Creates the `user_data` table in the `ALX_prodev` database if it does not already exist.
- Parameters:
  - `connection`: A MySQL connection object.

### `insert_data(connection, file_path)`
Inserts data from the CSV file (`user_data.csv`) into the `user_data` table.
- Parameters:
  - `connection`: A MySQL connection object.
  - `file_path`: Path to the `user_data.csv` file.

## Usage

### Prerequisites
- Python 3.x
- MySQL Server
- Python packages: `mysql-connector-python`

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/alx-backend-python.git
   cd alx-backend-python/python-generators-0x00

