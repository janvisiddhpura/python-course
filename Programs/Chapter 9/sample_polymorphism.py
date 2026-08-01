# Polymorphism concept
# same name, many forms = polymorphism
# Each animal class (Dog, Cat, Cow, Goat) has a method called `sound()` that outputs the sound made by that animal. 
# The program creates a list of animal objects and iterates through them, calling the `sound()` method for each one. 
# This shows how different classes can have methods with the same name but different implementations.
class Dog:
    def sound(self):
        print("Dog sound: Woof!")

class Cat:
    def sound(self):
        print("Cat sound: Meow!")

class Cow:
    def sound(self):
        print("Cow sound: Moo!")

class Goat:
    def sound(self):
        print("Goat sound: Baeeeee!")

animals = [Dog(), Cat(), Cow(), Goat()]
for item in animals:
    item.sound()