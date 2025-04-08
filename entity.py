# Base class
class Entity:
    def move(self):
        pass  # Placeholder for subclasses to implement

# Animal classes
class Dog(Entity):
    def move(self):
        print("Running 🐕")

class Fish(Entity):
    def move(self):
        print("Swimming 🐟")

# Vehicle classes
class Car(Entity):
    def move(self):
        print("Driving 🚗")

class Plane(Entity):
    def move(self):
        print("Flying ✈️")

# Function to test movement
def test_movement(entities):
    for entity in entities:
        entity.move()

# Create instances
entities = [Dog(), Fish(), Car(), Plane()]

# Test the movement behavior
test_movement(entities)
