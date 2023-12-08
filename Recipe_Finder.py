# Recipe_Finder.py

# Define a list of recipes
recipes = [
    {
        "name": "Spaghetti Bolognese",
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"],
        "instructions": "1. Cook spaghetti according to package instructions. \n2. In a large skillet, cook ground beef, onion, and garlic until browned. \n3. Add tomato sauce and simmer for 10 minutes. \n4. Serve sauce over cooked spaghetti."
    },
    {
        "name": "Chicken Stir-Fry",
        "ingredients": ["chicken breast", "bell pepper", "broccoli", "soy sauce", "ginger"],
        "instructions": "1. Cut chicken breast into small pieces. \n2. In a wok or large skillet, stir-fry chicken until cooked through. \n3. Add bell pepper, broccoli, soy sauce, and ginger. \n4. Stir-fry for another 5 minutes. \n5. Serve hot."
    },
    {
        "name": "Chocolate Chip Cookies",
        "ingredients": ["butter", "sugar", "flour", "chocolate chips", "vanilla extract"],
        "instructions": "1. Preheat oven to 350°F (175°C). \n2. In a mixing bowl, cream together butter and sugar. \n3. Add flour, chocolate chips, and vanilla extract. \n4. Mix until well combined. \n5. Drop spoonfuls of dough onto a baking sheet. \n6. Bake for 10-12 minutes. \n7. Allow cookies to cool before serving."
    }
]

# Function to search for recipes
def search_recipes(ingredient):
    matching_recipes = []
    for recipe in recipes:
        if ingredient in recipe["ingredients"]:
            matching_recipes.append(recipe)
    return matching_recipes

# Main program
if __name__ == "__main__":
    ingredient = input("Enter an ingredient: ")
    matching_recipes = search_recipes(ingredient)
    if matching_recipes:
        print(f"Recipes containing {ingredient}:")
        for recipe in matching_recipes:
            print(recipe["name"])
    else:
        print(f"No recipes found containing {ingredient}.")
