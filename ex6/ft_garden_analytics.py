class Plant:
    """Base plant class with common features."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant with name and height.

        Args:
            name: The name of the plant.
            height: The height of the plant in centimeters.
        """
        self.name = name
        self.height = height

    def grow(self) -> None:
        """Increment the plant's height by one centimeter."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """Return information about the plant.

        Returns:
            A string with plant information.
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Flowering plant class that inherits from Plant."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a FloweringPlant with parent attributes plus color.

        Args:
            name: The name of the flowering plant.
            height: The height of the plant in centimeters.
            color: The color of the flowers.
        """
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def get_info(self) -> str:
        """Return information about the flowering plant.

        Returns:
            A string with flowering plant information.
        """
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers "\
               f"({bloom_status})"


class PrizeFlower(FloweringPlant):
    """Prize-winning flower class that inherits from FloweringPlant."""

    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        """Initialize a PrizeFlower with parent attributes plus points.

        Args:
            name: The name of the prize flower.
            height: The height of the flower in centimeters.
            color: The color of the flower.
            prize_points: The number of prize points awarded.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        """Return information about the prize flower.

        Returns:
            A string with prize flower information.
        """
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers "\
               f"({bloom_status}), Prize points: {self.prize_points}"


class GardenManager:
    """Manager class for handling multiple gardens."""

    total_gardens = 0

    class GardenStats:
        """Nested class for calculating garden statistics."""

        def __init__(self) -> None:
            """Initialize GardenStats."""
            self.plants_added = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_flowers = 0

        def add_plant(self, plant: Plant) -> None:
            """Add a plant to statistics.

            Args:
                plant: The plant to add to statistics.
            """
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_flowers += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_plants += 1
            else:
                self.regular_plants += 1

        def record_growth(self, amount: int) -> None:
            """Record growth amount.

            Args:
                amount: The amount of growth to record.
            """
            self.total_growth += amount

        def get_report(self) -> str:
            """Generate statistics report.

            Returns:
                A formatted statistics report string.
            """
            return (f"Plants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant types: {self.regular_plants} regular, "
                    f"{self.flowering_plants} flowering, "
                    f"{self.prize_flowers} prize flowers")

    def __init__(self, owner_name: str) -> None:
        """Initialize a GardenManager.

        Args:
            owner_name: The name of the garden owner.
        """
        self.owner_name = owner_name
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden.

        Args:
            plant: The plant to add.
        """
        self.plants.append(plant)
        self.stats.add_plant(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self) -> None:
        """Make all plants in the garden grow."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            initial_height = plant.height
            plant.grow()
            self.stats.record_growth(plant.height - initial_height)

    def get_garden_score(self) -> int:
        """Calculate total garden score based on plant heights.

        Returns:
            The total score of the garden.
        """
        return sum(plant.height for plant in self.plants)

    def display_report(self) -> None:
        """Display a comprehensive garden report."""
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(self.stats.get_report())

    @classmethod
    def create_garden_network(cls, owner_names: list) -> list:
        """Create multiple gardens for a network.

        Args:
            owner_names: List of owner names for the gardens.

        Returns:
            List of GardenManager instances.
        """
        return [cls(name) for name in owner_names]

    @classmethod
    def get_total_gardens(cls) -> int:
        """Get the total number of gardens created.

        Returns:
            The total count of gardens.
        """
        return cls.total_gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate that a height value is acceptable.

        Args:
            height: The height value to validate.

        Returns:
            True if height is valid, False otherwise.
        """
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    # Create gardens
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    # Add plants to Alice's garden
    tree = Plant("Oak Tree", 100)
    flower = FloweringPlant("Rose", 25, "red")
    prize = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(tree)
    alice_garden.add_plant(flower)
    alice_garden.add_plant(prize)

    # Add plants to Bob's garden
    bob_garden.add_plant(Plant("Maple", 80))
    bob_garden.add_plant(FloweringPlant("Daisy", 12, "white"))

    # Make plants grow
    alice_garden.grow_all()

    # Display reports
    alice_garden.display_report()

    # Display garden scores
    print(f"\nGarden scores - Alice: {alice_garden.get_garden_score()}, "
          f"Bob: {bob_garden.get_garden_score()}")

    # Test static method
    print(f"Height validation test: "
          f"{GardenManager.validate_height(25)}")

    # Display total gardens
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
