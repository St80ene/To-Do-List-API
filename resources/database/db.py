import sqlite3


class DatabaseConnection:
    def __init__(self):
        self.db_connection = sqlite3.connect("db.py", check_same_thread=False)
        self.db_cursor = self.db_connection.cursor()

        pass

    def db_init(self):

        self.db_cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed BOOLEAN NOT NULL DEFAULT 0
        )
        """
        )

        self.db_connection.commit()


db = DatabaseConnection()

# Export only the connection and cursor if needed externally
__all__ = ["db"]
