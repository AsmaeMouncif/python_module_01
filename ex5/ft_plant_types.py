class Plant:
    """Base class representing a plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
            age: The age in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age
        
class Flower(Plant):
    """A class representing a flowering plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the flower.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def get_info(self) -> None:
        """Display information about the flower."""
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

    def bloom(self) -> None:
        """Display blooming message."""
        print(f"{self.name} is blooming beautifully!")
    
        
class Tree(Plant):
    """A class representing a tree."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        """Initialize a Tree.

        Args:
            name: The name of the tree.
            height: The height in centimeters.
            age: The age in days.
            trunk_diameter: The trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def get_info(self) -> None:
        """Display information about the tree."""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """Display the shade area provided by the tree."""
        shade_area: int = int((self.trunk_diameter * 20 / 100 / 2) ** 2 * 3.14)
        print(f"{self.name} provides {shade_area} square meters of shade")

class Vegetable(Plant):
    """A class representing a vegetable plant."""

    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
        """Initialize a Vegetable.

        Args:
            name: The name of the vegetable.
            height: The height in centimeters.
            age: The age in days.
            harvest_season: The harvest season.
            nutritional_value: The main nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> None:
        """Display information about the vegetable."""
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")

    def nutrition(self) -> None:
        """Display the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")
    
if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")


    rose.get_info()
    rose.bloom()

    print()
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 1000, 30)

    oak.get_info()
    oak.produce_shade()

    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 40, 70, "spring", "vitamin A")

    tomato.get_info()
    tomato.nutrition()