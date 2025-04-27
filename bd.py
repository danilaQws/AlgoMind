import sqlite3

con = sqlite3.connect("site.db")
curs = con.cursor()
sql = '''CREATE TABLE IF NOT EXISTS user_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT,
    name TEXT,
    age TEXT,
    image TEXT
)'''
curs.execute(sql)
con.close()


def enter(username, password):
    con = sqlite3.connect("site.db")
    curs = con.cursor()
    sql = "SELECT * FROM user_data WHERE username = ? AND password = ?"
    curs.execute(sql, (username, password))
    result = curs.fetchone()
    con.close()
    return bool(result)

