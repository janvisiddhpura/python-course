class Student:
    school_name = "ABC"
    i = 1
    # default constructor called when any new object is being created
    def __init__(self, name, semester):
        print("Default constructor!", Student.i)
        self.name = name
        self.semester = semester
        Student.i += 1

s1 = Student("JOHN", 5)
print("Student1 name:", s1.name)
print("Student1 semester:", s1.semester)

s2 = Student("PETER", 3)
print("Student2 name:", s2.name)
print("Student2 name:", s2.semester)

s3 = Student("JACK", 4)
print("Student3 name:", s3.name)
print("Student3 name:", s3.semester)