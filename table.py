#working on database, classes for the table
from Flask import render_template, request, redirect, url_for
from flask_table import Table, Col
from SQLalchemy import func
from pythondb import pythondb_bp
from pythondb.model import Users, Ingredients, Recipes_Names, Steps
from database_model import menus
from main import db

class UserTable(Table):
    recipenum = Col('recipenum')
    creator_name = Col('creator_name)

class RNTable(Table):
    recipenum = Col('recipenum')
    recipe_name = Col('recipe_name')

class ITable(Table):
    recipenum = Col('recipenum')
    ingredients = Col('ingredients')

class StepsTable(Table):
    recipenum = Col('recipenum')
    steps = Col('steps')

# connects default URL to a function
@pythondb_bp.route('/')
def databases():
  records=[]
  users=Users.query.all()
  for users in users:
    user_dict = {"recipenum": user.recipenum, "creator_name": user.creator_name}

    recipe_name = recipe_name.query.filter_by(recipenum=user.recipenum).first()

#need to figure out having multiple ingredients and steps inputs, how do we keep track of the data
