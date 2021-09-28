# Imports the only data object in data.json and names it Recipes
from .recipes import Recipes
# Import our test suite
from tests.unit_tests import TestGetNames
# Import stuff for the Custom 404 page not found handler
from flask import Flask
from flask import render_template
# Import the request object so that a user of the IP address can send data
from flask import request
app = Flask(__name__)


# app.route will only accept GET requests by default unless you add methods="POST" as a parameter
@app.get("/")
@app.get("/home")
@app.get("/index")
# The home view
def welcome():
  return "Welcome to Laily Ajellu's Assessment"

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

#------- Part 1 -------------
# Test with http://192.168.1.179:5000/recipes

# app.get Tells the browser to trigger the function below it when going on the webpage 
@app.get("/recipes")
def get_recipe_names():
    recipes = [recipe.get("name") for recipe in Recipes.load()]
    names_formatted = { "recipeNames": recipes}

    # Testing Part 1
    test_get_names = TestGetNames()
    test_get_names.output_equality(names_formatted)
    
    return names_formatted


#------- Part 2 -------------
# Test with http://192.168.1.179:5000/recipes/details/garlicPasta
# Return the details: ingredients and the number of steps in the recipe as JSON
# Using < > brackets, can have the recipe name as a variable

@app.get("/recipes/details/<name>")
def get_recipe_details(name):
  # If the recipe does not exists in data.json, the empty init dictionary is returned  
  webpage_output = {}
  
  # We defined Recipes.load() to return an array data type []
  loaded_recipes: list_type = Recipes.load()
  
  #Use Recipes class method: def get_details(cls, recipes: list, ingredient: str)
  recipe = Recipes.get_details(loaded_recipes, name)


  # If the recipe exists in data.json
  if recipe:
    webpage_output = {
      "details\n":{
        "ingredients": recipe.get("ingredients"),
        "numSteps": len(recipe.get("instructions"))
      }
    }

  return webpage_output

#------- Part 3 -------------
# Data passed in body using:
# http://192.168.1.80:5000/recipes?data={ "name": "butteredBagel", "ingredients": [ "1 bagel", "butter" ], "instructions": [ "cut the bagel", "spread butter on bagel" ] }
@app.post("/recipes")
def insert_recipe():
  # We defined Recipes.load() to return an array data type []
  loaded_recipes = Recipes.load()

  # get_json will parse the data as JSON that was the body of an object posted to a route.
  file_data = request.get_json()

  # Check if the recipe already exists
  existing_recipe = Recipes.get_details(loaded_recipes, file_data.get("name"))

  if existing_recipe:
    # Return multiple values with comma separation
    return {"Error" : "Recipe already exists"}, 400

  recipes.append(file_data)
  Recipes.write(recipes)

  return "", 201


