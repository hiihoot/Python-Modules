class Plant():
    """As usuale a constructor initing its attributes"""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


"""for testing purposes"""
print("=== Plant Factory Output ===")
Rose = Plant("Rose", 28, 30)
Sunflower = Plant("Sunflower", 80, 45)
Cactus = Plant("Cactus", 15, 120)
