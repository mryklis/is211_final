import sqlite3

DATABASE = 'blog.db'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

def create():
    qry = open('schema.sql').read()
    c.executescript(qry)
    conn.close()

if __name__ == '__main__':
    create()
    conn.close