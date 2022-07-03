# services/users/project/api/users/models.py


import datetime
import os

import jwt
from flask import Flask, current_app
from flask_mongoengine import MongoEngine
from mongoengine import (DateTimeField, Document, ListField, ReferenceField,
                         StringField, IntField)
from project import db
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'mongo',
    'host': 'nosql-db',
    'port': 27017
}
mongo = MongoEngine()
mongo.init_app(app)

class Feed(mongo.Document):
    content = StringField(max_length=140, required=True)
    user_id = IntField()
    created_at = mongo.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        return super(Feed, self).save(*args, **kwargs)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username="", email=""):
        self.username = username
        self.email = email


class Follow(db.Model):

    __tablename__ = "follows"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idol_id = db.Column(db.Integer, nullable=False)
    fan_id = db.Column(db.Integer, nullable=False)


class Timeline(db.Model):

    __tablename__ = "timelines"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    feed_id = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)


if os.getenv("FLASK_ENV") == "development":
    from project import admin
    from project.api.users.admin import UsersAdminView

    admin.add_view(UsersAdminView(User, db.session))
