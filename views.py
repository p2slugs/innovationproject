#This page is our views page in git which establishes app routes and renders html
#It is has the main navigation for our website
from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import aboutus


#title = data.setup() from app route /

app = Flask(__name__)
dbURI = 'sqlite:///models/myDB.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

@app.route('/')
def home_route():
    return render_template("base.html",)

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/p_overview')
def p_overview():
    return render_template('p_overview.html')

@app.route('/add_recipes')
def add_recipes():
    return render_template('add_recipes.html')

@app.route('/about')
def about():
    return render_template('about.html', aboutus=aboutus.about())

@app.route('/recipe_generator', methods=['GET','POST'])
#call to web api 
def recipe_generator():
  url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/extract"
  return render_template('recipe_generator.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

if __name__ == '__main__':
    app.run(debug=True, port='3000')
