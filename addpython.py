from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

dbURI = 'sqlite:///myrecipe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)


#we're adding to table recipes
class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    #not planning to delete scores, but still a good practice
    recipename = db.Column(db.String(20), unique=False, nullable=False)
    youringredients = db.Column(db.String(30), unique=False, nullable=False)
    steps = db.Column(db.String(15), unique=False, nullable=False)
    creator = db.Column(db.String(15), unique=False, nullable=False)
    #want score as int so we can sort by it easily.

    def __init__(self, recipename, youringredients, steps, creator):
        self.recipename = recipename
        self.youringredients = youringredients
        self.steps = steps
        self.creator = creator

    def __repr__(self):
        return f"{self.recipename},{self.youringredients},{self.steps},{self.creator}"

#create table
if __name__ == "__main__":
    """create each table"""
    db.create_all()
