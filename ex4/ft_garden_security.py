class SecurePlant():
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.set_height(starting_height)
        self.set_age(starting_age)
        print()

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_info(self):
        print()
        print(f"Current plant: {self.name} "
              f"({self.__height}cm, {self.__age} days)")


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 25, 30)

plant.set_height(-5)

plant.get_info()
