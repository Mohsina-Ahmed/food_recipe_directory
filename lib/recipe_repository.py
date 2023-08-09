from lib.recipes import *
class RecipeRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM recipes")
        recipes = []
        for row in rows:
            recipe = Recipes(row['id'], row['name'], row['cooking_time'], row['rating'])
            recipes.append(recipe)
        return recipes
    
    def find(self, recipe_id):
        rows = self._connection.execute("SELECT * FROM recipes WHERE id=%s", [recipe_id])
        row = rows[0]
        return Recipes(row['id'], row['name'], row['cooking_time'], row['rating'])
