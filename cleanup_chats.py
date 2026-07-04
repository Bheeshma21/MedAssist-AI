import sqlite3

conn = sqlite3.connect("database/medassist.db")
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM chat_sessions WHERE title='New Chat';"
)

conn.commit()

print(f"Deleted {cursor.rowcount} empty chats.")

conn.close()