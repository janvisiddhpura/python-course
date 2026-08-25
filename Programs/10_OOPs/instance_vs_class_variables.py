# instance:
# inside __init__: using self keyword
# class:
# inside class

class Student:

    # class variable
    school = "NY Public School"

    def __init__(self, name, marks, attendance):
        # instance variables
        self.name = name
        self.marks = marks
        self.attendance = attendance

    # instance method = as it reads instance variable
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

s1 = Student("Jack", 90, 79)
s2 = Student("Bob", 70, 10)

print(s1.calculate_grade())
print(s1.school)
print(s2.calculate_grade())
print(s2.school)