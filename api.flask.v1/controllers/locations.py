from flask import request, jsonify
from flask.views import MethodView
from models import Location
from db import db
from cerberus import Validator

class LocationAPI(MethodView):
    def get(self, id):
        if id is None:
            output = []
            for l in Location.query.all():
                loc_data = {}
                loc_data['id'] = l.id
                loc_data['zip'] = l.zip
                loc_data['text'] = l.text
                output.append(loc_data)
            return jsonify(output)
        else:
            location = Location.query.filter_by(id=id).one_or_none()
            if not location:
                return jsonify({'message' : 'Location not found'}), 404 

            loc_data = {}
            loc_data['id'] = location.id
            loc_data['zip'] = location.zip
            loc_data['text'] = location.text

            return jsonify(loc_data)

    def post(self):
        input_shema = Validator({'zip': {'type': 'string'}, 'text': {'type': 'string'}})
        data = request.get_json()

        if not input_shema.validate(data):
            return jsonify({'message' : 'Location zip and/or title missing'}), 400

        new_location = Location(zip=data['zip'], text=data['text'])
        db.session.add(new_location)
        db.session.commit()

        return jsonify({'message' : 'New location created!'}), 201

    def delete(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'}), 400
        
        location = Location.query.filter_by(id=id).one_or_none()
        if not location:
            return jsonify({'message' : 'Location not found'}), 404
        
        db.session.delete(location)
        db.session.commit()

        return jsonify({'message' : 'Location deleted'}), 202

    def put(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'}), 400

        input_shema = Validator({'zip': {'type': 'string'}, 'text': {'type': 'string'}})
        data = request.get_json()

        if not input_shema.validate(data):
            return jsonify({'message' : 'Location zip and/or title missing'}), 400

        location = Location.query.filter_by(id=id).one_or_none()
        if not location:
            return jsonify({'message' : 'Location not found'}), 404

        location.zip = data['zip']
        location.text = data['text']
        db.session.commit()

        return jsonify({'message' : 'Location updated'}), 202