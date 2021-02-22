#Backend Model CRUD Code

from sqlalchemy import func
from models import db, Recipes, Ingredients, Steps


# CRUD create/add a new record to the table
# user_dict{} expects username, password, email, phone_number
def model_create(user_dict):
    """prepare data for primary table extracting from form"""
    recipe = Recipes(recipe_name=user_dict["recipe_name"], creator=user_dict["creator"])
    """add and commit data to user table"""
    db.session.add(recipe)
    db.session.commit()
    """prepare data for related tables extracting from form and using new UserID """
    userid = db.session.query(func.max(Recipes.UserID))
    ingredients = Ingredients(ingredients=user_dict["email"], UserID=userid)
    steps = Steps(step=user_dict["steps"], UserID=userid)
    """email table add and commit"""
    db.session.add(ingredients)
    db.session.commit()
    """phone number table add and commit"""
    db.session.add(steps)
    db.session.commit()
