from flask import request, jsonify
from flask.views import MethodView
from models import Category
from db import db
from cerberus import Validator

class CategoryAPI(MethodView):
    def get(self, id):
        if id is None:
            output = []
            for cat in Category.query.all():
                cat_data = {}
                cat_data['id'] = cat.id
                cat_data['text'] = cat.text
                output.append(cat_data)
            return jsonify(output)
        else:
            category = Category.query.filter_by(id=id).one_or_none()
            if not category:
                return jsonify({'message' : 'Category not found'}), 404 

            cat_data = {}
            cat_data['id'] = category.id
            cat_data['text'] = category.text

            return jsonify(cat_data)

    def post(self):

        input_shema = Validator({'text': {'type': 'string'}})
        data = request.get_json()

        if not input_shema.validate(data):
            return jsonify({'message' : 'Category title missing'}), 400

        new_category = Category(text=data['text'])
        db.session.add(new_category)
        db.session.commit()

        return jsonify({'message' : 'New category created!'}), 201

    def delete(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'}), 400
        
        category = Category.query.filter_by(id=id).one_or_none()
        if not category:
            return jsonify({'message' : 'Category not found'}), 404
        
        db.session.delete(category)
        db.session.commit()

        return jsonify({'message' : 'Category deleted'}), 202

    def put(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'}), 400

        input_shema = Validator({'text': {'type': 'string'}})
        data = request.get_json()

        if not input_shema.validate(data):
            return jsonify({'message' : 'Category title missing'}), 400

        category = Category.query.filter_by(id=id).one_or_none()
        if not category:
            return jsonify({'message' : 'Category not found'}), 404

        category.text = data['text']
        db.session.commit()

        return jsonify({'message' : 'Category updated'}), 202