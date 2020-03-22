from db import db
from cerberus import Validator

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            }

    @staticmethod
    def fromJson(data):
        input_shema = Validator({'name': {'type': 'string'}})
        if not input_shema.validate(data):
            return None
        return Status(name=data['name'])