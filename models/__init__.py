#Model Definition Code

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from control import app

dbURI = 'sqlite:///models/myDB.db'

""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# declare the users database model
class Users(db.Model):
    recipe_num = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255), unique=True, nullable=False)
    creator = db.Column(db.String(255), unique=True, nullable=False)


# Declare emails database model
class Ingredients(db.Model):
    recipe_num = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.String(255), unique=True, nullable=False)


# declare phone numbers database model
class Steps(db.Model):
    recipe_num = db.Column(db.Integer, primary_key=True)
    steps = db.Column(db.String(255), unique=True, nullable=False)


# declare user account model
class AuthUser(UserMixin, db.Model):
    __tablename__ = 'authrecipe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)


#    def set_password(self, password):
#        """Create hashed password."""
#        self.password = generate_password_hash(password, method='sha256')

#    def check_password(self, password):
#        """Check hashed password."""
#       return check_password_hash(self.password, password)

#    def __repr__(self):
#        return '<AuthUser {}>'.format(self.username)
