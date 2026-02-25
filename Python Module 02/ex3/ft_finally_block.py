
def water_plants(plant_list):
    '''
    a function that simulates watering plants if there
    are some
    :param plant_list: a list
    '''
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant:
                print(f"Watering {plant}")
            else:
                raise ValueError("Cannot water None - Invalid plant!")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    '''
    test_watering_system for testing purpose
    '''
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    plants = ["tomato", None]
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
