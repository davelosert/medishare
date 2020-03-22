from flask import request, jsonify
from flask.views import MethodView
from models import Status
from db import db
from cerberus import Validator

class StatusAPI(MethodView):
    def get(self, id):
        if id is None:
            return jsonify([s.serialize for s in Status.query.all()])
        else:
            status = Status.query.filter_by(id=id).one_or_none()
            if not status:
                return jsonify({'message' : 'Status not found'}), 404 
            return jsonify(status.serialize)

    def post(self):
        new_status = Status.fromJson(request.get_json())
        if new_status is None:
            return jsonify({'message' : 'Status title missing'}), 400

        db.session.add(new_status)
        db.session.commit()

        return jsonify({'message' : 'New Status created!'}), 201

    def delete(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'}), 400
        
        status = Status.query.filter_by(id=id).one_or_none()
        if not status:
            return jsonify({'message' : 'Status not found'}), 404
        
        db.session.delete(status)
        db.session.commit()

        return jsonify({'message' : 'Status deleted'}), 202

    def put(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'}), 400

        input_shema = Validator({'text': {'type': 'string'}})
        data = request.get_json()

        if not input_shema.validate(data):
            return jsonify({'message' : 'Status title missing'}), 400

        status = Status.query.filter_by(id=id).one_or_none()
        if not status:
            return jsonify({'message' : 'Status not found'}), 404

        status.text = data['text']
        db.session.commit()

        return jsonify({'message' : 'Status updated'}), 202