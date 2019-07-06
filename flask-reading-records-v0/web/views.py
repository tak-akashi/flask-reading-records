# web/views.py
from web import app
from flask import render_template

@app.route('/')
def index():
    books = [{'title':'坂の上の雲', 'author':'司馬遼太郎', 'genre':'小説', 'date':'2018-06-01'},
             {'title':'竜馬がゆく', 'author':'司馬遼太郎', 'genre':'小説', 'date':'2017-12-31'},
             {'title':'ノーサイド・ゲーム', 'author':'池井戸潤', 'genre':'小説', 'date':'2019-06-30'}]
    return render_template('index.html', books=books)
