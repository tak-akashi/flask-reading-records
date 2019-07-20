from web import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    genre = db.Column(db.String(64), index=True)
    date = db.Column(db.Date)
    recommended = db.Column(db.Integer)
    comment = db.Column(db.String(256))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return '<Book {}>'.format(self.title)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True,unique=True)
    extras = db.Column(db.String(128))
    books = db.relationship('Book', backref='writer', lazy='dynamic')

    def __repr__(self):
        return '<Author {}>'.format(self.name)
