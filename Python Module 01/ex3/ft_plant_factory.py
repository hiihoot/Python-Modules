class Plant:
    counter = 0
    """As usuale a constructor initing its attributes"""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        Plant.counter += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


"""for testing purposes"""
print("=== Plant Factory Output ===")
Rose = Plant("Rose", 28, 30)
Qak = Plant("Qak", 200, 365)
Cactus = Plant("Cactus", 15, 120)
SunFlower = Plant("Sunflower", 80, 45)
Fern = Plant("Fern", 15, 120)

print(f"\nTotal plants created: {Plant.counter}")
