class Plant:
 '''
     This is the base class for different types of plants.
     inits attributes.
 '''   
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    '''
        Flower class inheriting from Plant
    '''
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")
        
    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    '''
       Tree class inheriting from Plant 
    '''
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_diameter} diameter")

    def produce_shade(self):
        print(f"{self.name} provides {int(3.14 * (self.height/100)**2)}"
              " square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.harvest_season} harvest")

    def nutritional_value(self):
        print(f"{self.name} is rich in vitamin C\n")


print("=== Garden Plant Types ===\n")
Rose = Flower("Rose", 25, 30, "red")
Rose.bloom()

Oak = Tree("Oak", 500, 1825, 50)
Oak.produce_shade()

Tomato = Vegetable("Tomato", 80, 90, "summer")
Tomato.nutritional_value()
