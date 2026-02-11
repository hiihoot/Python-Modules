class Plant():
    """initialize the plant attributes """
    def __init__(self, name: str, height: int, ages: int):
        self.name = name
        self.height = height
        self.ages = ages
        self.prev_age = ages
        self.prev_height = height
    """plant height increaser """
    def grow(self):
        self.height += 1
    """just like the height this increases the age"""
    def age(self):
        self.ages += 1
    """gets the info to be exactly like subject docs"""
    def get_info(self):
        print("=== Day 1 ===")
        print(f"{self.name}: {self.prev_height}cm, {self.prev_age} days old")
        print("=== Day 7 ===")
        print(f"{self.name}: {self.height}cm, {self.ages} days old")
        print(f"Growth this week: +{self.height - self.prev_height}cm")
        self.prev_age = self.ages
        self.prev_height = self.height


Rose = Plant("Rose", 25, 30)
x = 6
while x != 0:
    Rose.grow()
    Rose.age()
    x -= 1

Rose.get_info()
