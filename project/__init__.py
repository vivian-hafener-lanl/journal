# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
jrnl_db = SQLAlchemy() # Does this work? I guess I'll find out

# Is this where it needs to be? IDK
class journal(db.Model):
    id = jrnl_db.Column('entry_id', jrnl_db.Integer, primary_key = True)
    title = jrnl_db.Column(jrnl_db.String(100))
    time = jrnl_db.Column(jrnl_db.String(50))
    entry = jrnl_db.Column(jrnl_db.String(200))

    def __init__(self, time, title, entry):
        self.title = title
        self.time = time
        self.entry = entry

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app