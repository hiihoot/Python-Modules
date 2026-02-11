class SecurePlant():
    """this class used to protect data from corruption"""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name}")
    """Height setter it checks the value if valid first"""
    def set_height(self, new_value):
        if new_value >= 0:
            self._height = new_value
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted:"
                  f"height {new_value}cm [REJECTED]"
                  )
            print("Security: Negative height rejected")
    """Age setter the same as Height setter but for age"""
    def set_age(self, new_value):
        if new_value >= 0:
            self._age = new_value
            print(f"Age updated: {self._age} days [OK]")
        else:
            print(f"\nInvalid operation attempted:"
                  f"Age {new_value} days [REJECTED]"
                  )
            print("Security: Negative age rejected")
    """getters also yay!"""
    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


print("=== Garden Security System ===")
Plant = SecurePlant("Rose", 10, 30)
Plant.set_height(25)
Plant.set_age(30)
Plant.set_height(-5)
print(f"\nCurrent plant: {Plant.name}"
      f"({Plant.get_height()}cm {Plant.get_age()} days)"
      )
