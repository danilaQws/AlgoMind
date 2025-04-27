import sqlite3

con = sqlite3.connect("site.db")
curs = con.cursor()
sql = '''CREATE TABLE IF NOT EXISTS user_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT,
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

def add_user(username, data):
    con = sqlite3.connect("site.db")
    curs = con.cursor()
    sql = f"SELECT * FROM user_data WHERE username = '{login}'"
    curs.execute(sql)
    result = curs.fetchone()
    if result:
        return False
    else:
        sql = f''' INSERT INTO user_data (username, password, email) VALUES (?,?,?) ''', data
        curs.execute(sql)
        con.commit()
        con.close()
        return True