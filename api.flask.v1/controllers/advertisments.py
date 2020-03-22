from flask import request, jsonify
from flask.views import MethodView
from models import Advertisement
from db import db

class AdvertisementAPI(MethodView):
    def get(self, id):
        if id is None:
            return jsonify([a.serialize for a in Advertisement.query.all()])
        else:
            advertisement = Advertisement.query.filter_by(id=id).one_or_none()
            if not advertisement:
                return jsonify({'message' : 'Category not found'}), 404 
            return jsonify(advertisement.serialize)

    def post(self):
        new_advertisement = Advertisement.fromJson(request.get_json())
        if new_advertisement is None:
            return jsonify({'message' : 'Advertisement data missing or incomplete'}), 400

        db.session.add(new_advertisement)
        db.session.commit()

        return jsonify({'message' : 'New advertisement created!'}), 201

    def delete(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'}), 400
        
        advertisement = Advertisement.query.filter_by(id=id).one_or_none()
        if not advertisement:
            return jsonify({'message' : 'Advertisement not found'}), 404
        
        db.session.delete(advertisement)
        db.session.commit()

        return jsonify({'message' : 'Advertisement deleted'}), 202

    def put(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'}), 400
        
        new_advertisement = Advertisement.fromJson(request.get_json())
        if new_advertisement is None:
            return jsonify({'message' : 'Advertisement data missing or incomplete'}), 400

        advertisement = Advertisement.query.filter_by(id=id).one_or_none()
        if not advertisement:
            return jsonify({'message' : 'Advertisement not found'}), 404

        advertisement.topic = new_advertisement.topic
        advertisement.content = new_advertisement.content
        advertisement.quantity = new_advertisement.quantity
        advertisement.desiredAt = new_advertisement.desiredAt
        advertisement.category_id = new_advertisement.category_id
        advertisement.status_id = new_advertisement.status_id 
        db.session.commit()

        return jsonify({'message' : 'Advertisement updated'}), 202