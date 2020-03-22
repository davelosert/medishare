from flask import request, jsonify
from flask.views import MethodView
from models.advertisement import Advertisement

class AdvertisementAPI(MethodView):
    def get(self, id):
        if id is None:
            # return a list of users
            return jsonify({'message' : 'New user created!'})
        else:
            # expose a single user
            pass

    def post(self):
        # create a new user
        pass

    def delete(self, id):
        # delete a single user
        pass

    def put(self, id):
        # update a single user
        pass