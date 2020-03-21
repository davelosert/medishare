from db import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zip = db.Column(db.String(5), nullable=False)
    text = db.Column(db.String(100), nullable=False)