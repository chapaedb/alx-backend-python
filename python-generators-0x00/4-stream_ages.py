from seed import connect_to_prodev

def stream_user_ages():
    """
    Generator that fetches user ages from the database one by one.

    Yields:
        int: Age of a user.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']
    connection.close()

def calculate_average_age():
    """
    Calculates the average age of users using the stream_user_ages generator.

    Prints:
        str: Average age of users.
    """
    age_sum = 0
    count = 0
    for age in stream_user_ages():
        age_sum += age
        count += 1
    if count == 0:
        print("No users found.")
    else:
        print(f"Average age of users: {age_sum / count:.2f}")
