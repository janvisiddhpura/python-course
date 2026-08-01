# Student class with 3 marks and average method
class Student:

    def __init__(self, name, marks_list):
        self.name = name
        self.marks_list = marks_list

    def average(self):
        sum = 0
        for i in self.marks_list:
            sum += i
        print("Average:", sum/3)

s1 = Student("Bob", [90, 93, 83])
s1.average()
s2 = Student("William", [81, 90, 80])
s2.average()