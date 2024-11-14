import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

con.commit()
con.close()

