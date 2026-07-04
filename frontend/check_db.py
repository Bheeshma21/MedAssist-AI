import sqlite3

conn = sqlite3.connect("database/medassist.db")
cursor = conn.cursor()

print("=" * 60)
print("TABLES")
print("=" * 60)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"\nTable: {table_name}")

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"Rows : {count}")

print("\n" + "=" * 60)
print("DATABASE CHECK COMPLETED")
print("=" * 60)

conn.close()