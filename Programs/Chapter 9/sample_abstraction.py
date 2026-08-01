# data hiding = abstraction
# the program also uses the concept of inhetitance, where the derived classes (Dog, Cat, Cow, Goat) inherit from the base class (Animal).
from abc import ABC, abstractmethod

# using inheriting ABC(Abstract Base Class) to create an abstract class
class Animal(ABC):
    # this is an abstract method, it must be implemented in the derived class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    # while calling this method using objct without implementing the abstract method, it will raise an error
    # def make_sounds(self):
    #     print("Dog sound: Woof!")
    def sound(self):
            print("Dog sound: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat sound: Meow!")  

class Cow(Animal):
    def sound(self):
        print("Cow sound: Moo!")   

class Goat(Animal):
    def sound(self):
        print("Goat sound: Baeeeee!")

animals = [Dog(), Cat(), Cow(), Goat()]
for animal in animals:
    animal.sound()