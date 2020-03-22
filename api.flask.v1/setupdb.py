from medishare import initialize_app, app
from db import reset_database

initialize_app(app)
with app.app_context():
    reset_database()