class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days
        self.height_initial = height

    def age(self):
        self.age_days += 1

    def grow(self):
        self.height += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


plant = Plant("Rose", 25, 30)

print("=== Day 1 ===")
plant.get_info()

day = 0
while day < 6:
    plant.age()
    plant.grow()
    day += 1

print("=== Day 7 ===")
plant.get_info()

print(f"Growth this week: +{plant.height - plant.height_initial}cm")
