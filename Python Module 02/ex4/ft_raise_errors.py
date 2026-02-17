def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!\n")
        elif not (water_level >= 1 and water_level <= 10):
            if water_level > 10:
                raise ValueError(f"Error: Water level "
                                 f"{water_level} is too high (max 10)\n")
            else:
                raise ValueError(f"Error: Water level "
                                 f"{water_level} is too low (min 1)\n")
        elif not (sunlight_hours >= 2 and sunlight_hours <= 12):
            if sunlight_hours > 10:
                raise ValueError(f"Error: Sunlight hours "
                                 f"{sunlight_hours} is too high (max 10)\n")
            else:
                raise ValueError(f"Error: Sunlight hours "
                                 f"{sunlight_hours} is too low (min 2)")
        else:
            return f"Plant '{plant_name}' is healthy!\n"
    except ValueError as e:
        print(e)


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    print(check_plant_health("tomato", 5, 5))

    print("Testing empty plant name...")
    check_plant_health("", 5, 5,)

    print("Testing bad water level...")
    check_plant_health("tomato", 15, 10)

    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, 0)


if __name__ == "__main__":
    test_plant_checks()
