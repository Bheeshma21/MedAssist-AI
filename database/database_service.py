import sqlite3
from pathlib import Path


class Database:

    def __init__(self):

        # Create database folder
        Path("database").mkdir(exist_ok=True)

        # Connect
        self.conn = sqlite3.connect(
            "database/medassist.db",
            check_same_thread=False
        )

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

        # Enable foreign keys
        self.cursor.execute("PRAGMA foreign_keys = ON")

        # Create tables
        self.create_tables()

    # =====================================================
    # CREATE TABLES
    # =====================================================

    def create_tables(self):

        # ---------------- USERS ----------------
                # ---------------- UPLOADED FILES ----------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS uploaded_files(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER NOT NULL,

            file_type TEXT NOT NULL,

            file_name TEXT NOT NULL,

            file_path TEXT NOT NULL,

            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(session_id)
            REFERENCES chat_sessions(id)
            ON DELETE CASCADE

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            role TEXT DEFAULT 'patient',

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)
        

        # ---------------- CHAT SESSIONS ----------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_sessions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER NOT NULL,

            title TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE

        )
        """)

        # ---------------- MESSAGES ----------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER NOT NULL,

            user_id INTEGER NOT NULL,

            role TEXT,

            message TEXT,

            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(session_id)
            REFERENCES chat_sessions(id)
            ON DELETE CASCADE,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE

        )
        """)

        # ---------------- PATIENTS ----------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER UNIQUE,

            age INTEGER,

            gender TEXT,

            blood_group TEXT,

            allergies TEXT,

            medical_history TEXT,

            medications TEXT,

            emergency_contact TEXT,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE

        )
        """)

        # ---------------- REPORTS ----------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            report_name TEXT,

            report_type TEXT,

            file_path TEXT,

            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE

        )
        """)

        # ---------------- CREDITS ----------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS credits(

            user_id INTEGER PRIMARY KEY,

            remaining INTEGER DEFAULT 20,

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE

        )
        """)

        # ---------------- SETTINGS ----------------

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings(

            user_id INTEGER PRIMARY KEY,

            dark_mode INTEGER DEFAULT 0,

            notifications INTEGER DEFAULT 1,

            language TEXT DEFAULT 'English',

            FOREIGN KEY(user_id)
            REFERENCES users(id)
            ON DELETE CASCADE

        )
        """)

        self.conn.commit()
    # =====================================================
    # USER MANAGEMENT
    # =====================================================

    def create_user(
        self,
        name,
        email,
        password,
        role="patient"
    ):

        try:

            self.cursor.execute(
                """
                INSERT INTO users(

                    name,
                    email,
                    password,
                    role

                )

                VALUES(?,?,?,?)
                """,
                (
                    name,
                    email,
                    password,
                    role
                )
            )

            self.conn.commit()

            return True

        except sqlite3.IntegrityError:

            return False

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

    def update_credits(
        self,
        user_id,
        amount
    ):

        self.cursor.execute(
            """
            INSERT INTO credits(user_id, remaining)
            VALUES(?, ?)
            ON CONFLICT(user_id) DO UPDATE SET remaining = remaining + excluded.remaining
            """,
            (user_id, amount)
        )

        self.conn.commit()

    def login(
        self,
        email,
        password
    ):

        self.cursor.execute(
            """
            SELECT *

            FROM users

            WHERE
                email=?
            AND
                password=?
            """,
            (
                email,
                password
            )
        )

        return self.cursor.fetchone()
        # =====================================================
    # CHAT SESSIONS
    # =====================================================

    def create_chat_session(
        self,
        user_id,
        title="New Chat"
    ):

        self.cursor.execute(
            """
            INSERT INTO chat_sessions(

                user_id,
                title

            )

            VALUES(?,?)
            """,
            (
                user_id,
                title
            )
        )

        self.conn.commit()

        return self.cursor.lastrowid

    def get_chat_sessions(
        self,
        user_id
    ):

        self.cursor.execute(
            """
            SELECT

                id,
                title,
                created_at

            FROM chat_sessions

            WHERE user_id=?

            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        return self.cursor.fetchall()

    def get_chat_session(
        self,
        session_id
    ):

        self.cursor.execute(
            """
            SELECT *

            FROM chat_sessions

            WHERE id=?
            """,
            (session_id,)
        )

        return self.cursor.fetchone()

    def rename_chat_session(
        self,
        session_id,
        title
    ):

        self.cursor.execute(
            """
            UPDATE chat_sessions

            SET title=?

            WHERE id=?
            """,
            (
                title,
                session_id
            )
        )

        self.conn.commit()
    def rename_if_new_chat(
            self,
            session_id,
            title
    ):

           self.cursor.execute(
            """
            UPDATE chat_sessions

            SET title=?

            WHERE
                id=?
            AND
                title='New Chat'
            """,
            (
                title,
                session_id
            )
        )
           self.conn.commit()




    def delete_chat_session(
        self,
        session_id
    ):

        self.cursor.execute(
            """
            DELETE FROM chat_sessions

            WHERE id=?
            """,
            (session_id,)
        )

        self.conn.commit()
        # =====================================================
    # MESSAGES
    # =====================================================

    def save_message(
        self,
        user_id,
        role,
        message,
        session_id
    ):

        self.cursor.execute(
            """
            INSERT INTO messages(

                session_id,
                user_id,
                role,
                message

            )

            VALUES(?,?,?,?)
            """,
            (
                session_id,
                user_id,
                role,
                message
            )
        )

        self.conn.commit()

    def get_chat_history(
        self,
        user_id,
        session_id
    ):

        self.cursor.execute(
            """
            SELECT

                role,
                message,
                timestamp

            FROM messages

            WHERE
                user_id=?
            AND
                session_id=?

            ORDER BY id ASC
            """,
            (
                user_id,
                session_id
            )
        )

        return self.cursor.fetchall()

    def delete_chat_messages(
        self,
        session_id
    ):

        self.cursor.execute(
            """
            DELETE FROM messages

            WHERE session_id=?
            """,
            (session_id,)
        )

        self.conn.commit()
        # =====================================================
    # UPLOADED FILES
    # =====================================================

    def save_uploaded_file(
        self,
        session_id,
        file_type,
        file_name,
        file_path
    ):

        self.cursor.execute(
            """
            INSERT INTO uploaded_files(

                session_id,
                file_type,
                file_name,
                file_path

            )

            VALUES(?,?,?,?)
            """,
            (
                session_id,
                file_type,
                file_name,
                file_path
            )
        )

        self.conn.commit()

    def get_uploaded_files(
        self,
        session_id
    ):

        self.cursor.execute(
            """
            SELECT *

            FROM uploaded_files

            WHERE session_id=?

            ORDER BY uploaded_at DESC
            """,
            (session_id,)
        )

        return self.cursor.fetchall()

    def delete_uploaded_files(
        self,
        session_id
    ):

        self.cursor.execute(
            """
            DELETE FROM uploaded_files

            WHERE session_id=?
            """,
            (session_id,)
        )

        self.conn.commit()

    def get_latest_uploaded_file(
        self,
        session_id,
        file_type
    ):

        self.cursor.execute(
            """
            SELECT *

            FROM uploaded_files

            WHERE
                session_id=?
            AND
                file_type=?

            ORDER BY id DESC

            LIMIT 1
            """,
            (
                session_id,
                file_type
            )
        )

        return self.cursor.fetchone()
    # =====================================================
# DATABASE INSTANCE
# =====================================================

database = Database()