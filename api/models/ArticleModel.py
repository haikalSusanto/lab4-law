from . import db

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    rating_score =  db.Column(db.Integer)
    url = db.Column(db.String(250), unique=True, nullable=False)

    def __init__(self, author_id, rating_score, url):
        self.author_id = author_id
        self.rating_score = rating_score
        self.url = url

