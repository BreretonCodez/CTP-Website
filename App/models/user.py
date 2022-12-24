from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin, LoginManager

login_manager = LoginManager()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=True)
    lname = db.Column(db.String, nullable=True)
    email =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def toJSON(self):
        return{
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'email': self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))