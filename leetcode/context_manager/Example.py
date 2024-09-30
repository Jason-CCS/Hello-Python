# Problem 9 - context manager
# Write some examples using python context manager here.
import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        yield (cursor, conn)  # Provide the cursor for database operations
    finally:
        cursor.close()
        conn.close()

# Usage:
with db_connection('my_database.db') as db:
    # Create the table if it doesn't exist
    db[0].execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')
    # Insert some sample data
    db[0].execute("INSERT INTO my_table (name) VALUES ('Alice')")
    db[0].execute("INSERT INTO my_table (name) VALUES ('Bob')")
    db[1].commit()

    db[0].execute("SELECT * FROM my_table")
    results = db[0].fetchall()
    for row in results:
        print(row)