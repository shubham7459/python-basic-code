# Polymorphism Example in Python

# Class 1
class Dog:
    def action(self):
        print("Dog is barking 🐶")

# Class 2
class Cat:
    def action(self):
        print("Cat is meowing 🐱")

# Class 3
class Cow:
    def action(self):
        print("Cow is mooing 🐮")

# Function that uses polymorphism
def show_action(obj):
    obj.action()     # Calls action() of whichever object is passed

# Create objects
d = Dog()
c = Cat()
co = Cow()

# Use the same function with different objects
show_action(d)
show_action(c)
show_action(co)
