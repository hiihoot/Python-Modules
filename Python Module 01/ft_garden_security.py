class SecurePlant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age
    
    def set_height(self, new_value):
        if new_value < 0:
            self.height = new_value
            print(f"Height updated: {self.height} [OK]")
        else:
            print("Security: Negative height rejected")
    def set_age(self, new_value):
        if new_value < 0:
            self.age = new_value
            print(f"Age updated: {self.age} days [OK]")
            if self.height - self.age < 0:
                print(f"Invalid operation attempted: height {self.height - self.age}cm [REJECTED]")
        else:
            print("Security: Negative age rejected")
    def get_height(self):
        print(self.height)
    def get_age(self):
        return (self.age)

#continue here update the values! 

Rose = SecurePlant("name", 25, 30)
Rose.get_age()