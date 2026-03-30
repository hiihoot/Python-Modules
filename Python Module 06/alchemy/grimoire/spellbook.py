def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.validator import validate_ingredients
    if validate_ingredients(ingredients):
        return (f"Spell recorded: {spell_name} "
                f"({validate_ingredients(ingredients)})")
    else:
        return (f"Spell recorded: {spell_name} "
                f"({validate_ingredients(ingredients)})")
