class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print(f"{self.name}: {self.height}cm, {self.age} days old")


print("=== Garden Plant Registry ===")
Rose = Plant("Rose", 28, 30)
Sunflower = Plant("Sunflower", 80, 45)
Cactus = Plant("Cactus", 15, 120)
