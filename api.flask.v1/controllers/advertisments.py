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
        # delete a single user
        pass

    def put(self, id):
        # update a single user
        pass