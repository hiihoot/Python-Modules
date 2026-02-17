class GardenManager(Exception):
    def __init__(self, plant_list: list):
        self.plant_list = plant_list
        print("=== Garden Management System ===\n")

    def add_plants(self):
        try:
            print("Adding plants to garden...")
            for plant in self.plant_list:
                if plant != "":
                    print(f"added {plant} successfully")
                else:
                    raise ValueError("Error adding plant: "
                                     "Plant name cannot be empty!\n")
        except ValueError as e:
            print(e)

    def water_plants(self):
        try:
            print("Watering plants...")
            print("Opening watering system")
            for plant in self.plant_list:
                if plant != "":
                    print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        try:
            if plant_name == "":
                raise ValueError("Error: Plant name cannot be empty!\n")
            elif not (water_level >= 1 and water_level <= 10):
                if water_level > 10:
                    raise ValueError(f"Error checking {plant_name}: "
                                     f"Water level {water_level} "
                                     f"is too high (max 10)\n")
                else:
                    raise ValueError(f"Error checking {plant_name}:"
                                     f" Water level {water_level} "
                                     f"is too low (min 1)\n")
            elif not (sunlight_hours >= 2 and sunlight_hours <= 12):
                if sunlight_hours > 10:
                    raise ValueError(f"Error checking {plant_name}:"
                                     f"Sunlight hours {sunlight_hours} "
                                     f"is too high (max 10)\n")
                else:
                    raise ValueError(f"Error checking {plant_name}: "
                                     f"Sunlight hours {sunlight_hours} "
                                     f"is too low (min 2)")
            else:
                print(f"Plant '{plant_name}' is healthy "
                      f"(water: {water_level}, sun: {sunlight_hours})")
        except ValueError as e:
            print(e)

    def checking_erros(self):
        try:
            print("Testing error recovery...")
            raise ValueError("Caught GardenError: Not enough water in tank")
        except ValueError as e:
            print(e)
        finally:
            print("System recovered and continuing...")


if __name__ == "__main__":
    plants_list = ["tomato", "lettuce", ""]
    Manager = GardenManager(plants_list)
    Manager.add_plants()
    Manager.water_plants()
    print("Checking plant health...")
    Manager.check_plant_health("tomato", 5, 8)
    Manager.check_plant_health("lettuce", 15, 8)
    Manager.checking_erros()
    print("\nGarden management system test complete!")
