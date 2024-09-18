from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    cover_image = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Book {self.title}>"

