from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin, LoginManager
#from werkzeug.security import generate_password_hash, check_password_hash
#from control import app
from flask import Flask
app = Flask(__name__)

dbURI = 'sqlite:///models/myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
#app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
#login_manager = LoginManager()
#login_manager.init_app(app)