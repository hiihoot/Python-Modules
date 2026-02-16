class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


if __name__ == "__main__":
    try:
        print("Testing PlantError...")
        raise PlantError
    except PlantError:
        print("Caught PlantError: The tomato plant is wilting!\n")
    try:
        print("Testing WaterError...")
        raise WaterError
    except WaterError:
        print("Caught WaterError: Not enough water in the tank!\n")
    try:
        print("Testing catching all garden errors...")
        raise GardenError
    except (GardenError):
        print("Caught a garden error: The tomato plant is wilting!")
        print("Caught a garden error: Not enough water in the tank!\n")
    print("All custom error types work correctly!")
