# import sqlite3
from flask import Flask, render_template, request, redirect, session, flash

# DATABASE = 'blog.db'
# SECRET_KEY = 'LoremIpsum'
# USERNAME = 'maxim'
# PASSWORD = 'password'

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('/blog.html')

if __name__ == '__main__':
    app.run()