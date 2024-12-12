import aiosqlite
import asyncio

# Asynchronous function to fetch all users
async def async_fetch_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        print("Fetching all users...")
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
        return users

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        print("Fetching users older than 40...")
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            older_users = await cursor.fetchall()
        return older_users

# Asynchronous function to run both queries concurrently
async def fetch_concurrently(db_name):
    results = await asyncio.gather(
        async_fetch_users(db_name),
        async_fetch_older_users(db_name),
    )
    all_users, older_users = results
    print("\nAll Users:")
    for user in all_users:
        print(user)
    print("\nUsers Older Than 40:")
    for user in older_users:
        print(user)

# Database initialization for testing
async def initialize_db(db_name):
    async with aiosqlite.connect(db_name) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        await db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
        await db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 50))
        await db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Charlie", 25))
        await db.commit()

if __name__ == "__main__":
    db_name = "example_async.db"

    # Run the database initialization and queries concurrently
    asyncio.run(initialize_db(db_name))
    asyncio.run(fetch_concurrently(db_name))
