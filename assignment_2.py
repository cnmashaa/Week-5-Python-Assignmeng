class Car:
    def __init__(self, make):
        self.make = make  # The make of the car

    def move(self):
        print(f"{self.make} is driving on the road 🚗")

class Plane:
    def __init__(self, model):
        self.model = model  # The model of the plane

    def move(self):
        print(f"{self.model} is flying in the sky ✈️")

# Demonstrating polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()  # This will call the move method specific to the vehicle

# Create objects
car = Car("Toyota")
plane = Plane("Boeing 747")

# Call the same method on different objects
demonstrate_movement(car)  # Calls Car's move method
demonstrate_movement(plane)  # Calls Plane's move method
