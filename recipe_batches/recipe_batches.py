#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = float('inf')
  for ingredient, amount in recipe.items():
    amount_avail = ingredients.get(ingredient)
    enough = amount_avail // amount
    if not amount_avail or amount_avail - amount < 0:
      return 0
    elif enough < batches:
      batches = enough
  return batches 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))