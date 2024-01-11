# Our recipe matching algorithm utilises a priority queue data structure to effectively utilise expiring
# ingredients first.

import heapq

def input_ingredients_with_expiry():
    print("Enter each ingredient followed by days remaining before expiry (comma-separated, e.g., eggs,5,flour,10):")
    raw_input = input()
    ingredients_input = raw_input.split(',')
    ingredients_with_expiry = []

    for i in range(0, len(ingredients_input), 2):
        if i+1 < len(ingredients_input):
            ingredient = ingredients_input[i].strip()
            days = ingredients_input[i+1].strip()
            try:
                heapq.heappush(ingredients_with_expiry, (int(days), ingredient))
            except ValueError:
                print(f"Invalid format for days remaining for '{ingredient}'. Please enter a number.")
        else:
            print(f"Missing days remaining for '{ingredients_input[i]}'.")
    return ingredients_with_expiry

def find_matching_recipes(recipes, ingredients_with_expiry):
    matching_recipes = []
    ingredients = {ingredient for _, ingredient in ingredients_with_expiry}

    for recipe_name, recipe_ingredients in recipes.items():
        if all(ingredient in ingredients for ingredient in recipe_ingredients):
            matching_recipes.append(recipe_name)

    return matching_recipes

# Main program
print("Welcome to 'What's Fresh?' recipe suggester.")

# Pre-defined recipes
recipes = {'omelette': ['eggs', 'milk', 'cheese', 'salt', 'pepper'],
           'fried rice': ['rice', 'egg', 'oil', 'salt', 'pepper'],
           'scrambled eggs': ['eggs', 'milk', 'salt', 'pepper'],
           'pancakes': ['flour', 'eggs', 'milk', 'butter', 'sugar', 'salt'],
           'pad thai': ['rice noodles', 'chicken', 'tofu', 'eggs', 'peanuts', 'oil', 'sugar', 'fish sauce', 'lime', 'garlic', 'salt', 'pepper'],
           'chicken curry': ['chicken', 'coconut milk', 'curry paste', 'fish sauce', 'sugar', 'salt', 'pepper'],
           'chicken rice': ['chicken', 'rice', 'ginger', 'garlic', 'salt', 'pepper'],
           'nasi lemak': ['rice', 'coconut milk', 'anchovies', 'cucumber', 'egg', 'peanuts', 'sambal', 'salt', 'pepper'],
           'crab soup': ['crab', 'corn', 'egg', 'salt', 'pepper'],
           'crab fried rice': ['crab', 'rice', 'egg', 'salt', 'pepper'],
           'crab omelette': ['crab', 'egg', 'salt', 'pepper'],
           'crab curry': ['crab', 'coconut milk', 'curry paste', 'fish sauce', 'sugar', 'salt', 'pepper'],
           'thai basil chicken': ['chicken', 'basil', 'garlic', 'chilli', 'fish sauce', 'sugar', 'salt', 'pepper'],
           'thai basil pork': ['pork', 'basil', 'garlic', 'chilli', 'fish sauce', 'sugar', 'salt', 'pepper'],
           'thai basil beef': ['beef', 'basil', 'garlic', 'chilli', 'fish sauce', 'sugar', 'salt', 'pepper'],
           'thai basil seafood': ['seafood', 'basil', 'garlic', 'chilli', 'fish sauce', 'sugar', 'salt', 'pepper'],
           'mapo tofu': ['tofu', 'minced pork', 'chilli', 'garlic', 'salt', 'pepper'],
           'chicken satay': ['chicken', 'peanut sauce', 'cucumber', 'onion', 'salt', 'pepper'],
           'chicken wings': ['chicken wings', 'salt', 'pepper'],
           'chicken soup': ['chicken', 'salt', 'pepper'],
           'chicken porridge': ['chicken', 'rice', 'salt', 'pepper']
        }

ingredients_with_expiry = input_ingredients_with_expiry()
matching_recipes = find_matching_recipes(recipes, ingredients_with_expiry)

print("\nBased on your ingredients, you can cook:")
for recipe in matching_recipes:
    print(f"- {recipe}")
