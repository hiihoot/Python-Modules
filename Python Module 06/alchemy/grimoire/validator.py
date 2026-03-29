

def validate_ingredients(ingredients: str) -> str:
    elements = [
        "fire",
        "water",
        "earth",
        "air"
    ]
    ingredients.lower()
    for element in elements:
        if ingredients in element:
            return f"{ingredients} - Valid"
        else:
            return f"{ingredients} - INVALID"


print(validate_ingredients("fire air"))