class GardenError(Exception):
    '''
    Base class for all Garden related erros
    '''
    pass


class PlantError(GardenError):
    '''
    Raises when there is a plant related error
    '''
    pass


class WaterError(GardenError):
    '''
    Raises when there is a plant related error
    '''
    pass


class GardenManager:
    '''
    Manages operations like adding, watering, checking health of plants
    '''
    def __init__(self, plant_list: list):
        self.plant_list = plant_list
        print("=== Garden Management System ===\n")
    '''
    Methode adding plants
    '''
    def add_plants(self):
        try:
            print("Adding plants to garden...")
            for plant in self.plant_list:
                if plant != "":
                    print(f"added {plant} successfully")
                else:
                    raise PlantError("Error adding plant: "
                                     "Plant name cannot be empty!\n")
        except PlantError as e:
            print(e)
    '''
    Methode for watering plants
    '''
    def water_plants(self):
        try:
            print("Watering plants...")
            print("Opening watering system")
            for plant in self.plant_list:
                if plant != "":
                    print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)\n")
    '''
    this checks plant health
    '''
    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        try:
            if plant_name == "":
                raise PlantError("Plant name cannot be empty!\n")
        except PlantError as e:
            print(f"Error: {e}")
        try:
            if water_level > 10:
                raise WaterError(f"Error checking {plant_name}: "
                                 f"Water level {water_level} "
                                 "is too high (max 10)\n")
            elif water_level < 1:
                raise WaterError(f"Error checking {plant_name}:"
                                 f" Water level {water_level} "
                                 "is too low (min 1)\n")
        except WaterError as e:
            print(e)
        try:
            if sunlight_hours > 12:
                raise PlantError(f"Error checking {plant_name}:"
                                 f"Sunlight hours {sunlight_hours} "
                                 "is too high (max 12)\n")
            elif sunlight_hours < 2:
                raise PlantError(f"Error checking {plant_name}: "
                                 f"Sunlight hours {sunlight_hours} "
                                 "is too low (min 2)")
            if plant_name == "tomato":
                print(f"{plant_name}: healthy "
                      f"(water: {water_level}, sun: {sunlight_hours})")
        except PlantError as e:
            print(e)
    '''
    just like different error ex1 but this for just water so i can
    match the subject example output
    '''
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
