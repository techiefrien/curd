import sqlite3




con = sqlite3.connect("students.db")
cur = con.cursor()
cur.execute("delete  from students where id = ?",(4,))
val = cur.fetchall()
print(val)
con.commit()