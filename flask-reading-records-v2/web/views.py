# web/views.py
from web import app, db
from web.forms import BookForm
from web.models import Book
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    books = Book.query.order_by(Book.date.desc()).all()
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

@app.route('/<int:id>/update', methods=['GET','POST'])
def update_book(id):
    book = Book.query.get(id)

    form = BookForm()

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.genre = form.genre.data
        book.date = form.date.data
        db.session.commit()

        return redirect(url_for('index'))

    elif request.method == 'GET':
        form.title.data = book.title
        form.author.data = book.author
        form.genre.data = book.genre
        form.date.data = book.date

    return render_template('each_book.html', form=form, id=id)

@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))
