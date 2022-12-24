from App.models import User
from flask import render_template, url_for, redirect
import flask_login
from flask_login import login_user, logout_user, LoginManager
# from flask_jwt import JWT

login_manager = LoginManager()

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

@login_manager.unauthorized_handler
def no_auth():
    return redirect("/login")

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

def log_in_user(user, remember):
    return login_user(user, remember=remember)

def log_out_user():
    logout_user()

# Payload is a dictionary which is passed to the function by Flask JWT
'''def identity(payload):
    return User.query.get(payload['identity'])

def setup_jwt(app):
    return JWT(app, authenticate, identity)'''