import sqlite3


class PatientMemoryDB:

    def __init__(self):

        self.conn = sqlite3.connect(
            "database/patient_memory/patient_memory.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS patients(

            patient_id TEXT PRIMARY KEY,

            name TEXT,

            age INTEGER,

            gender TEXT,

            allergies TEXT,

            medical_history TEXT,

            medications TEXT

        )

        """)

        self.conn.commit()

    def save_patient(

        self,

        patient_id,

        name,

        age,

        gender,

        allergies,

        medical_history,

        medications

    ):

        self.cursor.execute("""

        INSERT OR REPLACE INTO patients
        VALUES(?,?,?,?,?,?,?)

        """,(

            patient_id,

            name,

            age,

            gender,

            ",".join(allergies),

            ",".join(medical_history),

            ",".join(medications)

        ))

        self.conn.commit()

    def get_patient(self, patient_id):

        self.cursor.execute("""

        SELECT * FROM patients
        WHERE patient_id=?

        """,(patient_id,))

        return self.cursor.fetchone()


memory_db = PatientMemoryDB()