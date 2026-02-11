class Plant:
    '''
    This is the base class for different types of plants.
    It initializes the common attributes: name and height.
    '''
    def __init__(self, name: str, height: int):
        self.name = name.capitalize()
        self.height = height

    '''
    This method displays the plant information'''
    def status(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    '''
    This class represents a Flowering Plant, inheriting from Plant.
    It initializes the color attribute.
    '''
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    '''
    Shows the status of the flowering plant
    '''
    def status(self) -> None:
        print(
            f"- {self.name}: {self.height}cm,",
            f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    '''
    This PrizeFlower class inherits from FloweringPlant.
    It initializes the points attribute.
    '''
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    '''
    Shows the status of the prize flower
    '''
    def status(self) -> None:
        print(
            f"- {self.name}: {self.height}cm, {self.color}",
            f"flowers (blooming), Prize points: {self.points}")


class Garden:
    '''
    This class represents a Garden.
    It initializes the name attribute and manages a list of plants.
    '''
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.plants = []
        self.total_plants = 0
        self.growth = 0

    '''
    This method adds a plant to the garden.
    And prints confirmation message.
    '''
    def add_plant(self, plant: Plant) -> None:
        print(f"Added {plant.name} to {self.name}'s garden")
        self.plants.append(plant)

    '''
    This method simulates growth for all plants in the garden.
    Each plant's height increases by 1cm.
    '''
    def grow_all_plants(self) -> None:
        print(f"\n{self.name} is helping all plants grow...")
        self.growth = 0
        for plant in self.plants:
            plant.height += 1
            self.growth += 1
            print(f"{plant.name} grew 1cm")


class GardenManager:
    '''
    This class manages represente a gardens network.
    It includes methods for garden statistics, validation, and reporting.
    '''

    '''
    This nested class provides statistics about the garden.
    It includes methods to count plants and types of plants.
    '''
    class GardenStats:
        def count_plants(plants) -> int:
            count = 0
            for plant in plants:
                count += 1
            return count
        count_plants = staticmethod(count_plants)

        def count_types(garden) -> dict:
            types = {'Plant': 0, 'FloweringPlant': 0, 'PrizeFlower': 0}
            for plant in garden.plants:
                types[plant.__class__.__name__] += 1
            return types
        count_types = staticmethod(count_types)

    gardens = []
    total = 0

    '''
    This class method creates a new garden network.
    It adds new agarden to the gardens list.
    And increments the total garden count.
    Returns the newly created garden.
    '''
    def create_garden_network(cls, name: str) -> Garden:
        new_garden = Garden(name)
        cls.gardens.append(new_garden)
        cls.total += 1
        return new_garden
    create_garden_network = classmethod(create_garden_network)

    '''
    This class method prints a report for the given garden.
    '''
    def print_garden_report(cls, garden: Garden) -> None:
        print(f"\n=== {garden.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            plant.status()
        types = cls.GardenStats.count_types(garden)
        print(
            f"\nPlants added: {cls.GardenStats.count_plants(garden.plants)},",
            f"Total growth : {garden.growth}cm")
        print(
            f"Plant types: {types['Plant']} regular,",
            f"{types['FloweringPlant']} flowering,",
            f"{types['PrizeFlower']} prize flowers\n")
    print_garden_report = classmethod(print_garden_report)

    '''
    This static method validates the heights of all plants in the garden.
    '''
    def validate_height(garden: Garden) -> bool:
        for plant in garden.plants:
            if plant.height < 0:
                return False
        return True
    validate_height = staticmethod(validate_height)

    '''
    This class method calculates the total score for each garden.
    '''
    def gardens_total_score(cls) -> dict:
        scores = {}
        for garden in cls.gardens:
            scores[garden.name] = 0
            for p in garden.plants:
                scores[garden.name] += p.height
        return scores
    gardens_total_score = classmethod(gardens_total_score)


def ft_garden_analytics() -> None:
    print("=== Garden Management System Demo ===\n")

    ''' Create a manger to handle gardens '''
    manager = GardenManager()

    ''' Create two gardens: alice's and Bob's '''
    alice = manager.create_garden_network("alice")
    bob = manager.create_garden_network("bob")

    ''' Add plants to alice's and bob's garden '''
    alice.add_plant(Plant("oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("sunflower", 50, "yellow", 10))
    bob.add_plant(Plant("flower", 92))

    ''' Grow all plants in alice's garden and print report '''
    alice.grow_all_plants()
    manager.print_garden_report(alice)

    ''' Validate heights in alice's garden and calculate scores '''
    print("Height validation test:", manager.validate_height(alice))
    scores = manager.gardens_total_score()

    ''' Print garden scores and total gardens managed '''
    print(
        "Garden scores - ",
        ", ".join(f"{k}: {v}" for k, v in scores.items()))
    print("Total gardens managed:", manager.total)


if __name__ == "__main__":
    ft_garden_analytics()
