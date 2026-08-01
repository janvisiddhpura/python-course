# the program has getter setter concept with encapsulation.
# encapsulation = data binding
# where the private attributes are accessed and modified using getter and setter methods.
class Person:
    def __init__(self, name, age):
        # private attribute with double underscore prefix
        self.__name = name
        self.__age = age

    # getter method for name
    def get_name(self):
        return self.__name

    # setter method for name
    def set_name(self, name):
        self.__name = name

    # getter method for age
    def get_age(self):
        return self.__age

    # setter method for age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

person1 = Person("Alice", 30)
# accessing private attributes using getter methods
print("Person1 Name:", person1.get_name())
print("Person1 Age:", person1.get_age())
# modifying private attribute using setter method
person1.set_age(35)  
# accessing modified private attribute using getter method
print("Person1 Updated Age:", person1.get_age())  

person2 = Person("Bob", 25)
# accessing private attributes using getter methods
print("\nPerson2 Name:", person2.get_name())
print("Person2 Age:", person2.get_age())
# modifying private attribute using setter method
person2.set_name("Robert")
# accessing modified private attribute using getter method
print("Person2 Updated Name:", person2.get_name())