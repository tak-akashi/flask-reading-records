# web/views.py
from web import app, db
from web.forms import BookForm
from web.models import Book
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/register', methods=['GET','POST'])
def register_book():
    form = BookForm()

    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, genre=form.genre.data, date=form.date.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register_book.html', form=form)
