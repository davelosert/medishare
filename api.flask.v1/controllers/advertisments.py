from flask import request, jsonify
from flask.views import MethodView
from models.advertisement import Advertisement

def get_advertisment():

    data = request.get_json()
    return jsonify({'message' : 'New user created!'})

def create_advertisment():
    if not current_user.admin:
        return jsonify({'message' : 'Cannot perform that function!'})

    data = request.get_json()

    #hashed_password = generate_password_hash(data['password'], method='sha256')

    new_adv = Advertisement()

    #new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    
    db.session.add(new_adv)
    db.session.commit()

    return jsonify({'message' : 'New user created!'})


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

    def put(self, user_id):
        # update a single user
        pass