
from api import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    city = db.Column(db.String(255))
    blood_group = db.Column(db.String(255))
    gender = db.Column(db.String(255))


class blood_request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_from = db.Column(db.Integer)
    request_to = db.Column(db.Integer)
    name = db.Column(db.String(255))
    status = db.Column(db.String(255), default="pending")
