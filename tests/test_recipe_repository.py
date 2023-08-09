from lib.recipe_repository import *
from lib.recipes import *
'''
When I get #all on the recipe repository
I get all the recipes back in the list 
'''

def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    result = repository.all()
    assert result == [
        Recipes(1, 'Shepard Pie', 30, 3),
        Recipes(2, 'Pizza', 30, 2),
        Recipes(3, 'Biriyani', 60, 1),
        Recipes(4, 'Fish Pie', 20, 3),
        Recipes(5, 'Lasagne', 40, 5)
    ]

'''
When i call #find with an index
it will return the rows corresponding to that index
'''
def test_find_from_index(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    result = repository.find(1)
    assert result == Recipes(1, 'Shepard Pie', 30, 3)

