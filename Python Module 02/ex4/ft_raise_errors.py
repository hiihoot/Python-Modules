def check_plant_health(plant_name, water_level, sunlight_hours):
    '''
    funtion for checkin plant health (name, water level, sunlight hours)
    :param plant_name: string
    :param water_level: int
    :param sunlight_hours: int
    '''
    try:
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!\n")
        if water_level > 10:
            raise ValueError(f"Error: Water level "
                             f"{water_level} is too high (max 10)\n")
        elif water_level < 1:
            raise ValueError(f"Error: Water level "
                             f"{water_level} is too low (min 1)\n")
        if sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours "
                             f"{sunlight_hours} is too high (max 12)\n")
        elif sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours "
                             f"{sunlight_hours} is too low (min 2)")
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
    print("\nAll error raising tests completed!")
