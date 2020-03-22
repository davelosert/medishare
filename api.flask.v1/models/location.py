from db import db
from cerberus import Validator

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zip = db.Column(db.String(5), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'zip': self.zip,
            'name': self.name,
            }
    
    @staticmethod
    def fromJson(data):
        input_shema = Validator({'zip': {'type': 'string'}, 'name': {'type': 'string'}})
        if not input_shema.validate(data):
            return None
        return Location(zip=data['zip'], name=data['name'])