class Plant:
    def __init__(self, name, heigth, age):
        self.name = name
        self.heigth = heigth
        self.age = age

    def show_info(self):
        print(f"{self.name}: {self.heigth}cm, {self.age} days old")

plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
]

print("=== Garden Plant Registry ===")

for i in range(len(plants)):
    plants[i].show_info()