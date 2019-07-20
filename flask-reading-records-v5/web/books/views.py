# web/books/views.py
from web import app, db
from web.forms import BookForm, BookUpdateForm
from web.models import Book, Author
from flask import render_template, redirect, url_for, request
from flask import Blueprint

books = Blueprint('books', __name__)

@books.route('/', methods=['GET'])
def index():
    books = Book.query.order_by(Book.date.desc()).paginate(page=1, per_page=app.config['ITEMS_PER_PAGE'], error_out=False)
    authors = db.session.query(Author).join(Book, Book.author_id == Author.id).all()
    return render_template('/books/index.html', books=books, authors=authors)

@books.route('/books/pages/<int:page_num>', methods=['GET','POST'])
def index_pages(page_num):

    books = Book.query.order_by(Book.date.desc()).paginate(page=page_num, per_page=app.config['ITEMS_PER_PAGE'], error_out=False)
    authors = db.session.query(Author).join(Book, Book.author_id == Author.id).all()
    return render_template('books/index.html', books=books, authors=authors)


@books.route('/books/register', methods=['GET','POST'])
def register():

    registered_authors = db.session.query(Author).order_by('name')
    authors_list = [(i.id, i.name) for i in registered_authors]

    form = BookForm()
    form.author.choices = authors_list

    if form.validate_on_submit():
        # book = Book(title=form.title.data, author=form.author.data, genre=form.genre.data, date=form.date.data)
        book = Book(title=form.title.data,genre=form.genre.data, date=form.date.data, recommended=form.recommended.data, comment=form.comment.data, author_id=form.author.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books.index'))
    return render_template('books/register.html', form=form)

@books.route('/books/<int:id>/update', methods=['GET','POST'])
def update(id):
    book = Book.query.get(id)

    registered_authors = db.session.query(Author).order_by('name')
    authors_list = [(i.id, i.name) for i in registered_authors]

    # form = BookForm()
    form = BookUpdateForm()

    form.author.choices = authors_list

    if form.validate_on_submit():

        # author = db.session.query(Author).filter(Author.id == form.author.data).first()
        book.title = form.title.data
        book.genre = form.genre.data
        book.author_id = form.author.data
        # book.author = author.name
        book.date = form.date.data
        book.recommended = form.recommended.data
        book.comment = form.comment.data
        db.session.commit()

        return redirect(url_for('books.index'))

    elif request.method == 'GET':

        form.title.data = book.title
        form.author.data = book.author_id
        form.genre.data = book.genre
        form.date.data = book.date
        form.recommended.data = book.recommended
        form.comment.data = book.comment

    return render_template('books/each.html', form=form, id=id)

@books.route('/books/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books.index'))
