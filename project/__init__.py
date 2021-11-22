# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

# init SQLAlchemy so we can use it later in our models

# def create_app():
APP = Flask(__name__)
db = SQLAlchemy(APP)

APP.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(APP)
# db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(APP)

from .models import User, Journal


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
APP.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .run import APP as app_blueprint
APP.register_blueprint(app_blueprint)

# return APP

