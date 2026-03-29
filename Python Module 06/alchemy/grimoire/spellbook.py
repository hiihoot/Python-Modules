from validator import validate_ingredients as validator


def record_spell(spell_name: str, ingredients: str) -> str:
    if validator(ingredients):
        return f"Spell recorded: {spell_name} ({validator(ingredients)})"
    else:
        return f"Spell recorded: {spell_name} ({validator(ingredients)})"
