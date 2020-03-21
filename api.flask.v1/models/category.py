from db import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50), nullable=False)