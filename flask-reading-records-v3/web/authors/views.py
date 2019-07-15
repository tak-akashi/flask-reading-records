# web/authors/views.py
from web import db
from web.forms import AuthorForm
from web.models import Book, Author
from flask import render_template, redirect, url_for, request
from flask import Blueprint

authors = Blueprint('authors', __name__)

@authors.route('/authors', methods=['GET'])
def index():
    authors = Author.query.order_by(Author.name).all()
    return render_template('/authors/index.html', authors=authors)

@authors.route('/authors/register', methods=['GET','POST'])
def register():
    form = AuthorForm()

    if form.validate_on_submit():
        check= Author.query.filter(Author.name == form.name.data).first()
        if check:
            errors = '既にこの著者は登録されています。他の著者名を登録してください。'
            return render_template('authors/register.html', form=form, errors=errors)

        author = Author(name=form.name.data, extras=form.extras.data)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('authors.index'))
    return render_template('authors/register.html', form=form)

@authors.route('/authors/<int:id>/update', methods=['GET','POST'])
def update(id):
    author = Author.query.get(id)

    form = AuthorForm()

    if form.validate_on_submit():
        check= Author.query.filter(Author.name == form.name.data).first()
        if check:
            errors = '既にこの著者は登録されています。他の著者名を登録してください。'
            return render_template('authors/register.html', form=form, errors=errors)

        author.name = form.name.data
        author.extras = form.extras.data
        db.session.commit()

        return redirect(url_for('authors.index'))

    elif request.method == 'GET':
        form.name.data = author.name
        form.extras.data = author.extras

    return render_template('authors/each.html', form=form, id=id)

@authors.route('/authors/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    author = Author.query.get(id)
    check = Book.query.filter(Book.author_id == id).first()
    if check:
        errors = "この著者による本を先に削除してください。"
        form = AuthorForm()
        form.name.data = author.name
        form.extras.data = author.extras
        return render_template('authors/each.html', form=form, id=id, errors=errors)
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('authors.index'))
