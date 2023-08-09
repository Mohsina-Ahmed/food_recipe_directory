from lib.recipes import *
"""
When I contruct a book store library
with the fields id, title and author name
They are reflected in the instance properties
"""

def test_construct_with_fields():
    recipe = Recipes(1, 'Shepard Pie', 30, 3)
    assert recipe.id == 1
    assert recipe.name == 'Shepard Pie'
    assert recipe.cooking_time == 30
    assert recipe.rating == 3

'''
When I contruct two receipes with the same fields
They are equal
'''
def test_equality():
    recipe1 = Recipes(1, 'Shepard Pie', 30, 3)
    recipe2 = Recipes(1, 'Shepard Pie', 30, 3)
    assert recipe1 == recipe2

"""
when I construct a book store 
And I format it to a string
Then it comes out in a friendly format
"""
def test_formatting():
    recipe = Recipes(1, 'Shepard Pie', 30, 3)
    assert str(recipe) == "Recipes(1, Shepard Pie, 30, 3)"
