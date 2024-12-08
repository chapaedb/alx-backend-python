from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database.

    Args:
        page_size (int): The number of rows per page.
        offset (int): The starting point for fetching rows.

    Returns:
        list: A list of rows as dictionaries.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """
    Lazily fetches pages of users from the database.

    Args:
        page_size (int): The number of rows per page.

    Yields:
        list: A page of rows as dictionaries.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break  # Exit when no more rows are fetched
        yield page
        offset += page_size
