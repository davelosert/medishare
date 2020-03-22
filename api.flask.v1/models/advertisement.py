from db import db
from datetime import datetime
from cerberus import Validator
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

    @property
    def serialize(self):    
        return {
            'id': self.id,
            'topic': self.topic,
            'content': self.content,
            'quantity': self.quantity,
            'desiredAt': datetime.strftime(self.desiredAt, '%m-%d-%Y'),
            'category': self.category.serialize,
            'status': self.status.serialize
            }
    
    @staticmethod
    def fromJson(data):
        input_shema = Validator({
            'topic': {'type': 'string'},
            'content': {'type': 'string'},
            'quantity': {'required': False, 'type': 'integer'},
            'desiredAt': {'required': False, 'type': 'string'},
            'category': {'required': False, 'type': 'dict', 'schema': {'id': {'type': 'integer'}}},
            'status': {'required': False, 'type': 'dict', 'schema': {'id': {'type': 'integer'}}}
        })
        if not input_shema.validate(data):
            return None

        return Advertisement(topic=data['topic'], content=data['content'], quantity=data['quantity'], 
                                desiredAt=datetime.strptime(data['desiredAt'], '%m-%d-%Y').date(), category_id=data['category']['id'], status_id=data['status']['id'])