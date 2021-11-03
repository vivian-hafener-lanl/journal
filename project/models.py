# models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Journal(db.Model):
    id = db.Column('entry_id', db.Integer, primary_key = True)
    u_id = db.Column(db.Integer)
    title = db.Column(db.String(100))
    time = db.Column(db.String(50))
    entry = db.Column(db.String(200))

    def __init__(self, u_id, title, time, entry):
        self.u_id = u_id
        self.title = title
        self.time = time
        self.entry = entry