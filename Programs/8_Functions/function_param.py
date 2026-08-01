# function parameters program

# function definition with default parameters
def average(a = 20, b = 40):
    avg = (a+b)/2
    print(avg)

# function calling with arguments
average(5, 10)
average(7, 10)
average(80, 99)
average(40, 70)
average()

# Write a function show_age(name, age) that prints: "abc is 21 years old."

def show_age(name, age):
    print(f"{name} is {age} years old.")

show_age("John", 20)
show_age("Peter", 24)