from flask import request, jsonify
from flask.views import MethodView
from models import Location
from db import db

class LocationAPI(MethodView):
    def get(self, id):
        if id is None:
            return jsonify([l.serialize for l in Location.query.all()])
        else:
            location = Location.query.filter_by(id=id).one_or_none()
            if not location:
                return jsonify({'message' : 'Location not found'}), 404 

            return jsonify(location.serialize)

    def post(self):
        new_location = Location.fromJson(request.get_json())
        if new_location is None:
            return jsonify({'message' : 'Location zip and/or title missing'}), 400

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


        new_location = Location.fromJson(request.get_json())
        if new_location is None:
            return jsonify({'message' : 'Category data missing or incomplete'}), 400

        location = Location.query.filter_by(id=id).one_or_none()
        if not location:
            return jsonify({'message' : 'Location not found'}), 404

        location.zip = new_location.zip
        location.name = new_location.name
        db.session.commit()

        return jsonify({'message' : 'Location updated'}), 202