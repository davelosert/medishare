from db import db

class Medical(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lanr = db.Column(db.String(9), nullable=False)

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship("Location")    