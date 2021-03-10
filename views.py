#This page is our views page in git which establishes app routes and renders html
#It is has the main navigation for our website
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import ingredients
from __init__ import app, db, User
from addpython import app, db, Recipe
import aboutus
import sqlite3 as sl3
import requests

# standard flask view support
from flask import render_template, request, redirect, url_for


@app.route('/generator', methods=['GET','POST'])
def generator():
    # call to random joke web api
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    response = requests.get(url)
    # formatting variables from return
    setup = response.json()[0]['setup']
    punchline = response.json()[0]['punchline']
    return render_template("generator.html",  setup=setup, punchline=punchline)

@app.route('/')
def home_route():
    return render_template("home.html",)

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/overview')
def p_overview():
    return render_template('overview.html')

@app.route('/addtable')
def addtable():
    return render_template('addtable.html')

@app.route('/about')
def about():
    return render_template('about.html', aboutus=aboutus.about())

#@app.route('/generator', methods=['GET','POST'])
#def generator():
   # conn = sl3.connect('recipe.db')
   # c = conn.cursor()
    #c.execute('SELECT * FROM RECIPES')
   # rows=c.fetchall()
    #print(rows)
  #  with conn:
    #    data = conn.execute('SELECT * FROM RECIPES')
   # for row in data:
    #    print(row)

    #return render_template('generator.html', rows=c.fetchall(), model=model.setup())


@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/form')
def form():
    return render_template('form.html')

# create/add a new record to the table
@app.route('/signup/', methods=["POST"])
def signup():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']


    new = User(name, email, phone, password)
    db.session.add(new)
    db.session.commit()

    #here for now, should go to scores eventually.
    return redirect(url_for('ingredients'))


# if login url, show phones table only
@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.form:
        # validation should be in HTML
        user_dict = {
            'name': request.form.get("txtUsername"),
            'email': request.form.get("txtEmail"),
            'phone': request.form.get("txtPhone"),
            'password': request.form.get("txtPassword")
        }
        if model_login(user_dict):
            return render_template('base.html')
        else:
            return "failed login"

    # if not logged in, show the login page
    return render_template("login.html")

# if login url, show phones table only
def model_login(user_dict):
    # Bypass if user is logged in
    #!
    if current_user.is_authenticated:
        return True
    # if not already logged in, show the login form
    print(user_dict['email'])
    user_record = User.query.filter_by(name=user_dict['name']).first()
    if user_record and User.check_password(user_record, user_dict['password']):
        login_user(user_record)
        return True
    # login failed
    return False

@app.route('/addrecipe/', methods=["POST"])
def addrecipe():
    recipename = request.form['recipename']
    youringredients = request.form['youringredients']
    steps = request.form['steps']
    creator = request.form['creator']

    new = Recipe(recipename, youringredients, steps, creator)
    db.session.add(new)
    db.session.commit()

    return render_template('addtable.html', recipename=recipename, youringredients=youringredients, steps=steps, creator=creator)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    return render_template('index.html', name=name, comment=comment)

@app.route('/easteregg')
def easteregg():
    return render_template('easteregg.html')

@app.route('/getupdates')
def getupdates():
    return render_template('getupdates')

@app.route('/sampleprojects')
def sampleprojects():
    return render_template('sampleprojects.html')

@app.route('/ingredients1')
def ingredients1():
    return render_template('ingredients1.html', ingredients=ingredients.ingredients())

@app.route('/customersupport')
def customersupport():
    return render_template('customersupport.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')
