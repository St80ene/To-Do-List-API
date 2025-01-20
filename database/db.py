import sqlite3

db_connection = sqlite3.connect("db.py", check_same_thread=False)
db_cursor = db_connection.cursor()


def db_init():

    db_cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed BOOLEAN NOT NULL DEFAULT 0
        )
        """
    )

    db_connection.commit()


db_init()

__all__ = ["db_connection", "db_cursor"]
