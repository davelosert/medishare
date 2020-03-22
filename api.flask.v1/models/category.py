from db import db
from cerberus import Validator

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            }

    @staticmethod
    def fromJson(data):
        input_shema = Validator({'name': {'type': 'string'}, 'image': { 'type': 'string'}})
        if not input_shema.validate(data):
            return None
        return Category(name=data['name'], image=data['image'])