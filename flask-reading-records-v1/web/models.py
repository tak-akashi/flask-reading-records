from web import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    author = db.Column(db.String(64), index=True)
    genre = db.Column(db.String(64), index=True)
    date = db.Column(db.Date)

    def __repr__(self):
        return '<Book {}>'.format(self.title)
