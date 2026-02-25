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


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}!\n")
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    try:
        print("Testing catching all garden errors...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
