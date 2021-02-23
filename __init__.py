from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

dbURI = 'sqlite:///recipe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)


#we're adding to table users
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    #not planning to delete scores, but still a good practice
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    phone = db.Column(db.String(15), unique=False, nullable=False)
    password = db.Column(db.String(15), unique=False, nullable=False)
    #want score as int so we can sort by it easily.

    def __init__(self, name, email,phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return f"{self.name},{self.email},{self.phone},{self.password}"

#create table
if __name__ == "__main__":
    """create each table"""
    db.create_all()
