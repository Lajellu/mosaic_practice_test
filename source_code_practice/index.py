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
# To send POST request from python 
import requests


# app.route will only accept GET requests by default unless you add methods="POST" as a parameter
@app.get("/")
@app.get("/home")
@app.get("/index")
# The home view
def welcome():
  print("On the welcome page")

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

    # TEST - Testing Part 1
    # test_get_names = TestGetNames() # Instantiate an object from the test class
    # test_get_names.output_equality(names_formatted)

    # DEBUG - Make a POST request for Part 3
    # dictToSend = { "name": "butteredBagel", "ingredients": [ "1 bagel", "butter" ], "instructions": [ "cut the bagel", "spread butter on bagel" ] }
    # response_given = requests.post('http://localhost:5000/recipes', json=dictToSend)
    # print("response from server:", response_given.text)

    # DEBUG - Make a PUT request for Part 4
    dictToSend = { "name": "butteredBagel", "ingredients": [ "1 bagel", "2 tbsp butter" ], "instructions": [ "cut the bagel", "spread butter on bagel" ] }
    response_given = requests.put('http://localhost:5000/recipes', json=dictToSend)
    print("response from server:", response_given.text)
    
    return names_formatted, 200


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

  return webpage_output, 200

#------- Part 3 -------------
# Data passed in body using:
# http://192.168.1.80:5000/recipes?data=
# JSON encoded as URL: %7B%0A%09%22name%22%3A%20%22butteredBagel%22%2C%20%0A%09%09%22ingredients%22%3A%20%5B%0A%09%09%09%221%20bagel%22%2C%20%0A%09%09%09%22butter%22%0A%09%09%5D%2C%20%0A%09%22instructions%22%3A%20%5B%0A%09%09%22cut%20the%20bagel%22%2C%20%0A%09%09%22spread%20butter%20on%20bagel%22%0A%09%5D%20%0A%7D%20
@app.post("/recipes")
def insert_recipe():
  # We defined Recipes.load() to return an array data type []
  loaded_recipes = Recipes.load()

  # get_json will parse the data as JSON that was the body of an object posted to a route.
  data_to_insert= request.get_json()

  # Check if the recipe already exists
  existing_recipe = Recipes.get_details(loaded_recipes, data_to_insert.get("name"))

  if existing_recipe:
    # Return multiple values with comma separation
    return {"Error" : "Recipe already exists"}, 400

  loaded_recipes.append(data_to_insert)
  Recipes.write(loaded_recipes)

  return "", 201


#------- Part 4 -------------
@app.put("/recipes")
def update_recipe():
  loaded_recipes = Recipes.load()
  data_for_update = request.get_json()

  existing_recipe = Recipes.get_details(loaded_recipes, data_for_update.get("name"))

  if not existing_recipe:
    return {"Error" : "Recipe does not exists, cannot be updated"}, 400

  else:
    Recipes.update(existing_recipe, data_for_update)
    Recipes.write(loaded_recipes)
    return "", 204