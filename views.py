#This page is our views page in git which establishes app routes and renders html
#It is has the main navigation for our website
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import ingredients
from __init__ import app
import aboutus
import sqlite3 as sl3
import requests



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
    return render_template("base.html",)

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/overview')
def p_overview():
    return render_template('overview.html')

@app.route('/add')
def add():
    return render_template('add.html')

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
