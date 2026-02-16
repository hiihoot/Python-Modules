
def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant:
                print(f"Watering {plant}")
            else:
                0/0
    except Exception:
        print("Error: Cannot water None - Invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
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
