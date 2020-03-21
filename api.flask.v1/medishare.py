from flask import Flask, request, jsonify, make_response
from db import db, reset_database
from models.user import User
from controllers import AdvertisementAPI, CategoryAPI

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

def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func, methods=['GET', 'PUT', 'DELETE'])

def initialize_app(thisapp):
    thisapp.config['SECRET_KEY'] = 'thisissecret'
    thisapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    db.init_app(thisapp)

def register_routes():
    register_api(AdvertisementAPI, 'advertisment_api', '/advertisments/')
    register_api(CategoryAPI, 'category_api', '/categories/')

def main():
    initialize_app(app)
    register_routes()
    app.run(debug=True)

if __name__ == '__main__':
    main()