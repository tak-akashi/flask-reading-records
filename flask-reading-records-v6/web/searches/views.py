# web/searches/views.py
from web import app, db
from web.forms import SearchForm
from web.models import Book, Author
from flask import render_template, redirect, url_for, request, Blueprint, session
import datetime

searches = Blueprint('searches', __name__)

@searches.route('/searches/', methods=['GET','POST'])
def index_search():

    registered_authors = db.session.query(Author).order_by('name')
    authors_list = [(0,"")]
    for i in registered_authors:
        authors_list.append([i.id, i.name])

    form = SearchForm()
    form.author.choices = authors_list

    if form.start_date.data is None:
        form.start_date.data = datetime.date(datetime.datetime.today().year,1,1)
    if form.end_date.data is None:
        form.end_date.data = datetime.datetime.today()

    if form.validate_on_submit():

        if form.author.data != 0:
            books = Book.query.filter(Book.title.like('%' + form.title.data + '%')).filter(Book.author_id==form.author.data).filter(Book.date>=form.start_date.data).filter(Book.date<=form.end_date.data)
        else:
            books = Book.query.filter(Book.title.like('%' + form.title.data + '%')).filter(Book.date>=form.start_date.data).filter(Book.date<=form.end_date.data)

        books = books.order_by(Book.date.desc()).paginate(page=1, per_page=app.config['ITEMS_PER_PAGE'], error_out=False)
        authors = db.session.query(Author).join(Book, Book.author_id == Author.id).all()

        session['title'] = form.title.data
        session['author'] = form.author.data
        session['start_date'] = form.start_date.data.strftime('%Y-%m-%d')
        session['end_date'] = form.end_date.data.strftime('%Y-%m-%d')

        return render_template('searches/search_results.html', books=books, authors=authors)
    return render_template('searches/search.html', form=form)

@searches.route('/searches/<int:page_num>', methods=['GET','POST'])
def search_results(page_num):

    form = SearchForm()

    form.title.data = session.get('title')
    form.author.data = session.get('author')
    form.start_date.data = datetime.datetime.strptime(session.get('start_date'),'%Y-%m-%d')
    form.end_date.data = datetime.datetime.strptime(session.get('end_date'),'%Y-%m-%d')

    if form.author.data != 0:
        books = Book.query.filter(Book.title.like('%' + form.title.data + '%')).filter(Book.author_id==form.author.data).filter(Book.date>=form.start_date.data).filter(Book.date<=form.end_date.data)
    else:
        books = Book.query.filter(Book.title.like('%' + form.title.data + '%')).filter(Book.date>=form.start_date.data).filter(Book.date<=form.end_date.data)
    books = books.order_by(Book.date.desc()).paginate(page=page_num, per_page=app.config['ITEMS_PER_PAGE'], error_out=False)
    authors = db.session.query(Author).join(Book, Book.author_id == Author.id).all()

    return render_template('searches/search_results.html', books=books, authors=authors)
