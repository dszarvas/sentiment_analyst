from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    text = db.Column(db.String, nullable=False)
    sentiment = db.Column(db.String, nullable=False)

    def __init__(self, date, text, sentiment):
        self.date = date
        self.text = text
        self.sentiment = sentiment

    def __repr__(self):
        return f'<History {self.id}: {self.date} - {self.sentiment}>'

def insert_history(date, text, sentiment):
    new_record = History(date, text, sentiment)
    db.session.add(new_record)
    db.session.commit()
