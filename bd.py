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
        )
'''

curs.execute(sql)
con.close()

def enter(username, password):
    con = sqlite3.connect("site.db")
    curs = con.cursor()
    sql = '''SELECT * FROM user_data WHERE username = {username} and password = {password}
    ''',(username,password)
    curs.execute(sql)
    result = curs.fetchone()
    con.close()
    if result:
        return True
    else:
        return False

    