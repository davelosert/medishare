from db import db
from datetime import datetime
    
class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    desiredAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship("Category")

    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    status = db.relationship("Status")