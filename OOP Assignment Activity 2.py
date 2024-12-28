# Activity 2: Polymorphism Challenge

# Step 1: Creating a base class "Vehicle"
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Step 2: Creating derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Bicycle(Vehicle):
    def move(self):
        return "Cycling 🚴"

# Testing Activity 2
vehicles = [Car(), Plane(), Bicycle()]

for vehicle in vehicles:
    print(vehicle.move())