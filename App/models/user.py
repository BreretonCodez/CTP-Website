from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin, LoginManager

login_manager = LoginManager()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def toJSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    # def get_id()
    # def is_active()
    # def is_anonymous()
    # def is_authenticated()

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))