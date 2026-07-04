import sqlite3
from pathlib import Path


class Database:

    def __init__(self):

        Path("database").mkdir(exist_ok=True)

        self.connection = sqlite3.connect(
            "database/medassist.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        # Users
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            full_name TEXT,

            email TEXT UNIQUE,

            password TEXT,

            role TEXT

        )
        """)

        # Chat History
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            email TEXT,

            role TEXT,

            message TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        self.connection.commit()

    # ----------------------
    # User Functions
    # ----------------------

    def create_user(
        self,
        full_name,
        email,
        password,
        role
    ):

        self.cursor.execute(
            """
            INSERT INTO users
            (
                full_name,
                email,
                password,
                role
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                full_name,
                email,
                password,
                role
            )
        )

        self.connection.commit()

    def get_user(self, email):

        self.cursor.execute(

            """
            SELECT *
            FROM users
            WHERE email=?
            """,

            (email,)

        )

        return self.cursor.fetchone()

    # ----------------------
    # Chat Functions
    # ----------------------

    def save_message(
        self,
        email,
        role,
        message
    ):

        self.cursor.execute(
            """
            INSERT INTO conversations
            (
                email,
                role,
                message
            )
            VALUES (?, ?, ?)
            """,
            (
                email,
                role,
                message
            )
        )

        self.connection.commit()

    def get_history(self, email):

        self.cursor.execute(
            """
            SELECT role,message
            FROM conversations
            WHERE email=?
            ORDER BY id
            """,
            (email,)
        )

        return self.cursor.fetchall()


database = Database()