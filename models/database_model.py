#from main.py import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect
app = Flask(__name__)

#database setup 
dbURI = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

# declare the users database model
class Users(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    creator_name = db.Column(db.String(255), unique=True, nullable=False)

# Declare ingredients database model
class Ingredients(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.String(255), unique=True, nullable=False)

#Declare the recipe title database model
class Recipe_Names(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String(255), unique=True, nullable=False)
 
#Declare the steps database model
class Steps(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    steps = db.Column(db.String(255), unique=True, nullable=False)
 
 #table creation 
db.create_all()

#inspect table
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))
