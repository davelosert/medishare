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
                return jsonify({'message' : 'Category not found'})

            cat_data = {}
            cat_data['id'] = category.id
            cat_data['text'] = category.text

            return jsonify(cat_data)

    def post(self):

        input_shema = Validator({'text': {'type': 'string'}})
        data = request.get_json()

        if not input_shema.validate(data):
            return jsonify({'message' : 'Category title missing'})

        new_category = Category(text=data['text'])
        db.session.add(new_category)
        db.session.commit()

        return jsonify({'message' : 'New category created!'})

    def delete(self, id):
        if id is None:
            return jsonify({'message' : 'Invalid request'})
        
        category = Category.query.filter_by(id=id).one_or_none()
        if not category:
            return jsonify({'message' : 'Category not found'})
        
        db.session.delete(category)
        db.session.commit()

        return jsonify({'message' : 'Category deleted'})

    def put(self, id):

        input_shema = Validator({'text': {'type': 'string'}})
        data = request.get_json()

        if not input_shema.validate(data):
            return jsonify({'message' : 'Category title missing'})

        category = Category.query.filter_by(id=id).one_or_none()
        if not category:
            return jsonify({'message' : 'Category not found'})

        category.text = data['text']
        db.session.commit()

        return jsonify({'message' : 'Category updated'})