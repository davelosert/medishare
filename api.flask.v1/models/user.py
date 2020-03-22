from db import db
from models import Medical

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    mail = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    medical_id = db.Column(db.Integer, db.ForeignKey('medical.id'))
    medical = db.relationship("Medical")