from App.models import User
from App.database import db

# Creates a new user
def create_user(email, password):
    newuser = User(email=email, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

# Updates a current user

def update_user(id, email):
    user = get_user(id)
    if user:
        user.email = email
        db.session.add(user)
        return db.session.commit()
    return None

#U User Accessors
def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_id(id):
    return User.query.filter_by(id=id).first()

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users
    