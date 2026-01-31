class Plant:
    """Base class for all plants."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
        """
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        """Increase plant height by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> None:
        """Display plant information."""
        print(f"{self.name}: {self.height}cm")
        

class FloweringPlant(Plant):
    """Plant that can flower."""

    def __init__(self, name: str, height: int, flower_color: str, is_blooming: bool) -> None:
        """Initialize a FloweringPlant.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
            flower_color: The color of the flowers.
            is_blooming: Whether the plant is blooming.
        """
        super().__init__(name, height)
        self.flower_color: str = flower_color
        self.is_blooming: bool = is_blooming

    def get_info(self) -> None:
        """Display flowering plant information."""
        state: str = "blooming" if self.is_blooming else "not blooming"
        print(f"{self.name}: {self.height}cm, {self.flower_color} flowers ({state})")


class PrizeFlower(FloweringPlant):
    """Special flowering plant with prize points."""

    def __init__(self, name: str, height: int, flower_color: str, is_blooming: bool, prize_points: int) -> None:
        """Initialize a PrizeFlower.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
            flower_color: The color of the flowers.
            is_blooming: Whether the plant is blooming.
            prize_points: The prize points for the flower.
        """
        super().__init__(name, height, flower_color, is_blooming)
        self.prize_points: int = prize_points

    def get_info(self) -> None:
        """Display prize flower information."""
        state: str = "blooming" if self.is_blooming else "not blooming"
        print(f"{self.name}: {self.height}cm, {self.flower_color} flowers ({state}), Prize points: {self.prize_points}")


class Garden:
    """Garden that contains multiple plants."""

    def __init__(self, owner: str) -> None:
        """Initialize a Garden.

        Args:
            owner: The name of the garden owner.
        """
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.total_plants_added: int = 0
        self.total_growth: int = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        self.total_plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self) -> None:
        """Help all plants in the garden grow."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def garden_report(self) -> None:
        """Generate comprehensive garden report."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end="")
            plant.get_info()
        stats = self.GardenStats(self)
        regular, flowering, prize = stats.count_types()
        print()
        print(f"Plants added: {self.total_plants_added}, Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

    def validate_heights(self) -> bool:
        """Check if all plants have valid heights."""
        return all(plant.height >= 0 for plant in self.plants)

    def calculate_score(self) -> int:
        """Calculate total garden score."""
        score: int = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score
        """Calculate total garden score"""
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score
    
    class GardenStats:
        """Nested class for calculating garden statistics"""
        def __init__(self, garden):
            self.garden = garden
            
        def count_plants(self):
            """Count total number of plants"""
            return len(self.garden.plants)
            
        def total_height(self):
            """Calculate total height of all plants"""
            total = 0
            for plant in self.garden.plants:
                total += plant.height
            return total
            
        def count_types(self):
            """Count different types of plants"""
            plant_count = 0
            flowering_count = 0
            prize_count = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize_count += 1
                elif isinstance(plant, FloweringPlant):
                    flowering_count += 1
                elif isinstance(plant, Plant):
                    plant_count += 1
            return plant_count, flowering_count, prize_count


class GardenManager:
    """Manager for handling multiple gardens with analytics."""

    _network_managers: list['GardenManager'] = []

    def __init__(self, owner: str) -> None:
        """Initialize a GardenManager.

        Args:
            owner: The name of the manager.
        """
        self.owner: str = owner
        self.gardens: list[Garden] = []
        GardenManager._network_managers.append(self)

    def add_garden(self, garden: Garden) -> None:
        """Add a garden to the manager (instance method)."""
        self.gardens.append(garden)

    def grow_all_gardens(self) -> None:
        """Grow all plants in all managed gardens (instance method)."""
        for garden in self.gardens:
            garden.grow_all_plants()

    def total_gardens(self) -> int:
        """Return total number of managed gardens (instance method)."""
        return len(self.gardens)

    @classmethod
    def create_garden_network(cls, owner_name: str, garden_owners: list[str]) -> 'GardenManager':
        """Create a network of gardens with a single manager (class method).

        Args:
            owner_name: The name of the manager.
            garden_owners: List of garden owner names.
        Returns:
            GardenManager instance with gardens added.
        """
        manager = cls(owner_name)
        for garden_owner in garden_owners:
            garden = Garden(garden_owner)
            manager.add_garden(garden)
        return manager

    @staticmethod
    def validate_garden_name(name: str) -> bool:
        """Utility function to validate garden owner names (static method).

        Args:
            name: The name to validate.
        Returns:
            True if valid, False otherwise.
        """
        if not name or not isinstance(name, str):
            return False
        return len(name) > 0 and name.strip() == name

    class GardenStats:
        """Nested class for calculating statistics across multiple gardens."""

        def __init__(self, manager: 'GardenManager') -> None:
            """Initialize GardenStats.

            Args:
                manager: The GardenManager instance.
            """
            self.manager: GardenManager = manager

        def total_plants(self) -> int:
            """Count total plants across all gardens."""
            total: int = 0
            for garden in self.manager.gardens:
                total += len(garden.plants)
            return total

        def average_garden_size(self) -> float:
            """Calculate average number of plants per garden."""
            if len(self.manager.gardens) == 0:
                return 0.0
            return self.total_plants() / len(self.manager.gardens)

        def total_score(self) -> int:
            """Calculate total score across all gardens."""
            total: int = 0
            for garden in self.manager.gardens:
                total += garden.calculate_score()
            return total


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
        
    # Create plants with inheritance chain
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    # Create Alice's garden
    alice_garden = Garden("Alice")
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    print()
        
    # Create manager and add garden
    manager = GardenManager("Admin")
    manager.add_garden(alice_garden)
        
    # Grow all plants
    manager.grow_all_gardens()
    print()

    # Generate report
    alice_garden.garden_report()
    print()

    # Validate heights
    print("Height validation test:", alice_garden.validate_heights())

    # Create Bob's garden
    bob_garden = Garden("Bob")
    bob_garden.add_plant(Plant("Cactus", 40))
    bob_garden.add_plant(FloweringPlant("Tulip", 20, "pink", False))
    manager.add_garden(bob_garden)

    # Calculate and display scores
    print(f"Garden scores - Alice: {alice_garden.calculate_score()}, Bob: {bob_garden.calculate_score()}")
    print("Total gardens managed:", manager.total_gardens())