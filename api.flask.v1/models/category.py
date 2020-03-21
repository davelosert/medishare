from db import db
from cerberus import Validator

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            }

    @staticmethod
    def fromJson(data):
        input_shema = Validator({'text': {'type': 'string'}})
        if not input_shema.validate(data):
            return None
        return Category(text=data['text'])