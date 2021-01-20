#This page is our views page in git which establishes app routes and renders html
#It is has the main navigation for our website
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from __init__ import app
import aboutus


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

@app.route('/generator', methods=['GET','POST'])
#call to web api 
def generator():
  url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/extract"
  return render_template('generator.html')

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


