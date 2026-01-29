class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        
    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
    
        
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        canopy_diameter = self.trunk_diameter * 20 / 100
        shade_area = (canopy_diameter / 2) ** 2 * 3.14
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        
        print(f"{self.name} is rich in {self.nutritional_value}")
    
if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 150, 90, "yellow")
    
    rose.get_info()
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 60)
    
    print()
    oak.get_info()
    oak.produce_shade()
    
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 60, 70, "spring", "vitamin A")
    
    print()
    tomato.get_info()