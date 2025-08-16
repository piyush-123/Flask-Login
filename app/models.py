from extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150),unique=True,nullable=False)
    email = db.Column(db.String(150),unique=True,nullable=False)
    password_hash = db.Column(db.String(256),nullable=False)
    confirmed = db.Column(db.Boolean,default=False)
    failed_logins = db.Column(db.Integer,default = 0)
    last_failed_at = db.Column(db.DateTime,nullable=True)
    created_at = db.Column(db.DateTime,default=datetime.timezone.utc)