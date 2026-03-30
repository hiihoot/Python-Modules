

def validate_ingredients(ingredients: str) -> str:
    elements = [
        "fire",
        "water",
        "earth",
        "air"
    ]

    for item in ingredients.split():
        if item not in elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
