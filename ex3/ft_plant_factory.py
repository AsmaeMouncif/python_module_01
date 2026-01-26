class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age_days} days)")


plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120),
]

print("=== Plant Factory Output ===")

count = 0
for i in plants:
    i.get_info()
    count += 1

print()
print(f"Total plants created: {count}")
