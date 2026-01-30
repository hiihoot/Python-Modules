def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "grams":
        end = "total"
    elif unit == "area":
        end = "square meters"
        print(f"{seed_type.capitalize()} seeds: covers {quantity} {end}")
    elif unit == "packets":
        end = "available"
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} {end}")
    else:
        print(f"{seed_type.capitalize()} seeds: {quantity} Unknown unit type ")
