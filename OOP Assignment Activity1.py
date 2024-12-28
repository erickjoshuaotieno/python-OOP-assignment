# Assignment 1: Design Your Own Class

# Step 1: Creating a class representing a "Smartphone"
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def browse_internet(self):
        return f"Browsing internet on {self.brand} {self.model}..."

    def __str__(self):
        return f"Smartphone({self.brand}, {self.model}, {self.storage}GB, {self.battery_life}hrs)"

# Step 2: Adding an inheritance layer
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def play_game(self, game):
        return f"Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system."

    def browse_internet(self):
        return f"Browsing internet in gaming mode on {self.brand} {self.model}..."

# Testing Assignment 1
phone = Smartphone("Apple", "iPhone 15", 256, 20)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 512, 18, "advanced vapor chamber")

print(phone)
print(phone.make_call("+1234567890"))
print(phone.browse_internet())

print(gaming_phone)
print(gaming_phone.play_game("Call of Duty"))
print(gaming_phone.browse_internet())


