class Plant:
    """Base class for all garden plants."""

    def __init__(self, name, height):
        """Initialize name, height, and type."""
        self.name = name
        self.height = height
        self.p_type = "regular"

    def grow(self):
        """Increase height by 1."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        """Return basic string representation."""
        return f"{self.name}: {self.height}cm"

    def get_score(self):
        """Return score based on height."""
        return self.height


class FloweringPlant(Plant):
    """Child class for plants with flowers."""

    def __init__(self, name, height, color):
        """Initialize with parent attributes and flower color."""
        super().__init__(name, height)
        self.color = color
        self.p_type = "flowering"

    def get_info(self):
        """Override info to include flower details."""
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Grandchild class for competition-grade flowers."""

    def __init__(self, name, height, color, points):
        """Initialize with points for scoring."""
        super().__init__(name, height, color)
        self.points = points
        self.p_type = "prize"

    def get_info(self):
        """Override info to include prize points."""
        base = super().get_info()
        return f"{base}, Prize points: {self.points}"

    def get_score(self):
        """Override score to include bonus points."""
        return self.height + self.points


class GardenManager:
    """Manages multiple gardens and provides analytics."""

    total_gardens = 0

    class GardenStats:
        """Internal helper for tracking growth and counts."""

        def __init__(self):
            """Initialize stats counters."""
            self.plants_added = 0
            self.total_growth = 0

        def record_addition(self):
            """Track new"""
            self.plants_added += 1

        def record_growth(self):
            """Track growth"""
            self.total_growth += 1

    def __init__(self, owner):
        """Setup manager with owner and stats."""
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        """Validate height and add plant to collection"""
        if GardenManager.validate_height(plant.height):
            self.plants.append(plant)
            self.stats.record_addition()
            print(f"Added {plant.name} to {self.owner}'s garden")
        else:
            print(f"Error: Invalid height for {plant.name}.")

    def help_plants_grow(self):
        """Grow every plant in the garden."""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def garden_report(self):
        """Generate analytics report without using isinstance()."""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        counts = {"regular": 0, "flowering": 0, "prize": 0}
        total_score = 0

        for plant in self.plants:
            print(f"- {plant.get_info()}")
            total_score += plant.get_score()
            counts[plant.p_type] += 1

        print(f"\nPlants added: {self.stats.plants_added}, "
              f"Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {counts['regular']} regular, "
              f"{counts['flowering']} flowering, "
              f"{counts['prize']} prize flowers\n")
        return total_score

    def create_garden_network(cls):
        """Class method to start the demo."""
        print("=== Garden Management System Demo ===\n")
    create_garden_network = classmethod(create_garden_network)

    def validate_height(height):
        """Static method to check height value."""
        return height > 0
    validate_height = staticmethod(validate_height)


if __name__ == "__main__":
    GardenManager.create_garden_network()

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    # bach nwesl 218 daruri 130 ula 4i 30 fl hieght probably
    oak = Plant("Oak Tree", 130)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.help_plants_grow()
    score_alice = alice.garden_report()

    bob.add_plant(Plant("Cactus", 42))
    bob.add_plant(FloweringPlant("Lily", 50, "white"))
    score_bob = bob.garden_report()

    print(f"Garden scores - Alice: {score_alice}, Bob: {score_bob}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
