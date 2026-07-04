import sqlite3


class HealthTimeline:

    def __init__(self):

        self.conn = sqlite3.connect(
            "database/medassist.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_timeline(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            report_name TEXT,

            report_type TEXT,

            health_score INTEGER,

            risk_level TEXT,

            dashboard_json TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def save_report(
        self,
        user_id,
        report_name,
        report_type,
        health_score,
        risk_level,
        dashboard_json
    ):

        self.cursor.execute(
            """
            INSERT INTO health_timeline(

                user_id,
                report_name,
                report_type,
                health_score,
                risk_level,
                dashboard_json

            )

            VALUES(?,?,?,?,?,?)
            """,
            (
                user_id,
                report_name,
                report_type,
                health_score,
                risk_level,
                dashboard_json
            )
        )

        self.conn.commit()

    def get_reports(
        self,
        user_id
    ):

        self.cursor.execute(
            """
            SELECT *

            FROM health_timeline

            WHERE user_id=?

            ORDER BY created_at ASC
            """,
            (user_id,)
        )

        return self.cursor.fetchall()


health_timeline = HealthTimeline()