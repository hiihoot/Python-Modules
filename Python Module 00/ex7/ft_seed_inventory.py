def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: "
              f"covers {quantity} square meters")
    elif unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    else:
        print("Unknown unit type")
