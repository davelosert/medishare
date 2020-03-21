from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database():
    from models import advertisement, category, location, medical, status, user
    db.drop_all()
    db.create_all()