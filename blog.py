import sqlite3
from flask import Flask, render_template, request, redirect, session, flash

DATABASE = 'blog.db'
SECRET_KEY = 'LoremIpsum'
USERNAME = 'maxim'
PASSWORD = 'password'

app = Flask(__name__)
app.config.from_object(__name__)

def get_posts():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''select ID, TITLE, PDATE, AUTHOR, BLOG from POSTS ORDER BY PDATE DESC''')
    posts = [dict(id=row[0], title=row[1], pdate=row[2], author=row[3], blog=row[4][0:200]) for row in c.fetchall()]
    conn.close()
    return posts


@app.route('/', methods=['GET'])
def index():
    return render_template('/blog.html', posts=get_posts())

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME or request.form['password'] != PASSWORD:
            error = 'Invalid Login Credentials'
            return render_template('/login.html', error=error)
        else:
            session['logged_in'] = True
            return redirect('/dashboard')
    else:
        return render_template('login.html', error=error)

@app.route('/read_post/<id>', methods=['GET'])
def read(id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('select TITLE, PDATE, AUTHOR, BLOG from POSTS where ID = ?', (id))
    results = [dict(title=row[0], pdate=row[1], author=row[2], blog=row[3]) for row in c.fetchall()]
    conn.close()
    return render_template('/read_post.html', results=results)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if session['logged_in'] != True:
        return redirect('/login')
    else:
        return render_template('/dashboard.html', posts=get_posts())


@app.route('/edit_post/<id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('select ID, TITLE, PDATE, AUTHOR, BLOG from POSTS where ID = ?', (id,))
    results = [dict(id=row[0], title=row[1], pdate=row[2], author=row[3], blog=row[4]) for row in c.fetchall()]

    if session['logged_in'] != True:
        return redirect('/login')
    else:
        if request.method == 'GET':
            return render_template('/edit_post.html', posts=results)
        else:
            conn = sqlite3.connect(DATABASE)
            c = conn.cursor()
            c.execute('select ID, TITLE, PDATE, AUTHOR, BLOG from POSTS where ID = ?', (4,))
            results = [dict(id=row[0], title=row[1], pdate=row[2], author=row[3], blog=row[4]) for row in c.fetchall()]
            print(results)
            dic = results[0]
            id = dic['id']
            print(id)
            title = dic['title']
            print(title)
            pdate = dic['pdate']
            print(pdate)
            author = dic['author']
            print(author)
            text = str(request.form['post'])
            print(text)
            # c.execute('''UPDATE POSTS SET TITLE = ?, PDATE = ?, AUTHOR = ?, BLOG = ? where ID = ?''',
            #           (results['title'], results['pdate'], results['author'], text, results['id']))
            # conn.commit()
            # conn.close()
            return redirect('/dashboard')


if __name__ == '__main__':
    app.run()