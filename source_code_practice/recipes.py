import json

class Recipes:
	JSON_FILE = "data.json"

	@classmethod
	def load(cls):
		# open() is a built in function of python for opening files
		with open(cls.JSON_FILE, "r") as recipesFile:
			# json.load deserializes a file and returns a JSON Object, 
			# jsonObject.get specifies which objects to get and return as an array
			return json.load(recipesFile).get("recipes", [])

	@classmethod
	def get_details(cls, recipes: list, name: str):
		# json.get will get the data.json name objects that match the name given in URL

		recipe_exists = lambda recipe_requested : True if (recipe_requested.get("name") == name) else False
		# filter is a python native function takes a BOOL and a LIST OF OBJECTS
		filtered_recipes = filter(recipe_exists, recipes)
		# next is a python native function that returns the next item in the list, None: no default value given
		first_match = next(filtered_recipes, None)
		return first_match

	@classmethod
	def write(cls, recipes: list):
		with open(cls.JSON_FILE, "w") as recipesFile:
			# The data.json file already contains an object called recipes
			# dump will append the new recipe(s) to the rest of the list
			# json.dump({"addThis": fromThisVariable)}, fromThisFile, indent=2) 
			json.dump({"recipes": recipes}, recipesFile, indent=2) 

	@classmethod
	def update(cls, existing_recipe: dict, data_for_update: dict):
		for key, val in data_for_update.items():
			existing_recipe[key] = val

