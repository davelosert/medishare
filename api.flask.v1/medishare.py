from flask import Flask, request, jsonify, make_response
from db import db, reset_database
from models.user import User
from controllers.advertisments import AdvertisementAPI, create_advertisment, get_advertisment

app = Flask(__name__)

@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

def initialize_app(thisapp):
    thisapp.config['SECRET_KEY'] = 'thisissecret'
    thisapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    db.init_app(thisapp)

    #thisapp.add_url_rule("/advertisments", "advertisments", get_advertisment, methods=['GET'])
    #thisapp.add_url_rule("/advertisments", "newadvertisment", create_advertisment, methods=['POST'])

    adv_view = AdvertisementAPI.as_view('advertisment_api')
    app.add_url_rule('/advertisments/', defaults={'id': None}, view_func=adv_view, methods=['GET'])
    app.add_url_rule('/advertisments/', view_func=adv_view, methods=['POST'])
    app.add_url_rule('/advertisments/<int:id>', view_func=adv_view, methods=['GET', 'PUT', 'DELETE'])

def main():
    initialize_app(app)
    app.run(debug=True)

if __name__ == '__main__':
    main()