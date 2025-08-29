# Activity 1: Smartphone Class with Inheritance

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact}...")

    def install_app(self, app):
        print(f"Installing {app} on {self.brand} {self.model}.")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB)"


# Inheritance Example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"Playing {game} smoothly on {self.brand} {self.model} with {self.cooling_system} cooling system.")


# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 256)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "liquid cooling")

# Using methods
print(phone1)
phone1.call("Alice")
phone1.install_app("WhatsApp")

print(phone2)
phone2.play_game("PUBG Mobile")


# Activity 2: Polymorphism Example

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("Driving on the road!")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water!")


# Demonstrating polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
