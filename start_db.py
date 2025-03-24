import sqlite3

conn = sqlite3.connect("database.db")

with open ("schema.sql") as f :
    conn.executescript(f.read())


conn.execute('INSERT INTO posts (title,content) VALUES (?,?)', ("Asmaa" ,  "my first post") )
conn.execute('INSERT INTO posts (title,content) VALUES (?,?)', ("Second post" ,  "😂") )

conn.commit()   
conn.close()