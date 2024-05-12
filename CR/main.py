import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, age INTEGER NOT NULL);
''')
con.commit()

cur.execute("INSERT INTO users(name, age) VALUES(?, ?)",("Алексей", 30))
cur.execute("INSERT INTO users(name, age) VALUES(?, ?)",("Игорь", 25))

con.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
print(rows)
con.close()

