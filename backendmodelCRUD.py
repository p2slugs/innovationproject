#Backend Model CRUD Code

from sqlalchemy import func
from models import db, Users, Ingredients, Steps


# CRUD create/add a new record to the table
# user_dict{} expects username, password, ingredients, steps
def model_create(user_dict):
    """prepare data for primary table extracting from form"""
    user = Users(recipe_name=user_dict["recipe_name"], creator=user_dict["creator"])
    """add and commit data to user table"""
    db.session.add(user)
    db.session.commit()
    """prepare data for related tables extracting from form and using new UserID """
    userid = db.session.query(func.max(Users.UserID))
    ingredient = Ingredients(ingredient_=user_dict["ingredient"], UserID=userid)
    steps = Steps(steps=user_dict["steps"], UserID=userid)
    """ingredient table add and commit"""
    db.session.add(ingredient)
    db.session.commit()
    """phone number table add and commit"""
    db.session.add(steps)
    db.session.commit()


# CRUD read: filter single record in table based off of userid
# userid required
def model_read(userid):
    """filter users by userid"""
    user = Users.query.filter_by(UserID=userid).first()
    user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
    """filter ingredient by userid"""
    ingredient = Ingredients.query.filter_by(UserID=userid).first()
    if ingredient:
        user_dict['ingredients'] = ingredient.ingredient_
    """filter phone number by userid"""
    pn = Steps.query.filter_by(UserID=userid).first()
    if pn:
        user_dict['steps'] = pn.steps
    return user_dict


# CRUD update
# user_dict{} expects userid, ingredient, steps
def model_update(user_dict):
    """fetch userid"""
    userid = user_dict["userid"]
    """update ingredient in table from data in form if it exists, insert if not"""
    if Ingredients.query.filter_by(UserID=userid).first() is not None:
        db.session.query(Ingredients).filter_by(UserID=userid).update({Ingredients.ingredient_: user_dict["email"]})
    else:
        ingredient = Ingredients(ingredient_=user_dict["ingredient"], UserID=userid)
        db.session.add(ingredient)
    """update phone number in table from data in form"""
    if Steps.query.filter_by(UserID=userid).first() is not None:
        db.session.query(Steps).filter_by(UserID=userid).update(
            {Steps.step: user_dict["step"]})
    else:
        step = Steps(step=user_dict["step"], UserID=userid)
        db.session.add(step)

    """commit changes to database"""
    db.session.commit()


# CRUD delete
# userid required
def model_delete(userid):
    """fetch userid"""
    userid = userid
    """delete userid rows from ingredients table"""
    db.session.query(Ingredients).filter(Ingredients.UserID == userid).delete()
    """delete userid rows from phone numbers table"""
    db.session.query(Steps).filter(Steps.UserID == userid).delete()
    """delete userid rows from users table"""
    db.session.query(Users).filter(Users.UserID == userid).delete()
    """commit changes to database"""
    db.session.commit()


# CRUD read: query all tables and records in the table
def model_query_all():
    """convert Users table into a list of dictionary rows"""
    records = []
    users = Users.query.all()
    for user in users:
        user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
        # filter ingredient
        ingredient = Ingredients.query.filter_by(UserID=user.UserID).first()
        if ingredient:
            user_dict['ingredients'] = ingredient.ingredient_
        # filter phone number
        pn = Steps.query.filter_by(UserID=user.UserID).first()
        if pn:
            user_dict['steps'] = pn.step
        # append to records
        records.append(user_dict)
    return records


# CRUD read: query ingredients table
def model_query_ingredients():
    # fill the table with ingredients only
    records = []
    ingredients = Ingredients.query.all()
    for ingredient in ingredients:
        user_dict = {'id': ingredient.UserID, 'ingredients': ingredient.ingredient_}
        records.append(user_dict)
    return records


# CRUD read: query phones table
def model_query_phones():
    # fill the table with phone numbers only
    records = []
    steps = Steps.query.all()
    for phone in steps:
        user_dict = {'id': phone.UserID, 'steps': phone.step}
        records.append(user_dict)
    return records