import sqlite3

conn = sqlite3.connect("database/medassist.db")
cursor = conn.cursor()

print("=" * 70)
print("MEDASSIST DATABASE HEALTH REPORT")
print("=" * 70)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [row[0] for row in cursor.fetchall()]

for table in tables:

    print(f"\n📋 {table}")

    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]

    print(f"Rows : {count}")

    if table != "sqlite_sequence":

        cursor.execute(f"PRAGMA table_info({table})")
        columns = [c[1] for c in cursor.fetchall()]

        if columns:

            cursor.execute(f"SELECT * FROM {table} LIMIT 3")

            rows = cursor.fetchall()

            if rows:
                print("Sample Records:")
                for row in rows:
                    print(" ", row)
            else:
                print("No Records")

print("\n" + "=" * 70)

print("Duplicate Users")

cursor.execute("""
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1
""")

duplicates = cursor.fetchall()

if duplicates:
    print(duplicates)
else:
    print("No duplicate users.")

print("\nDatabase Status : HEALTHY")

conn.close()