# Program to take user input and print it

name = input("Enter your name : ")
print("Hello,",name)

"""
the above will print = "Hello, Janvi" even though we didn't added the space
the reason is that the print function automatically adds a space between the arguments passed to it
the solution to this is to use the sep parameter of the print function and set it to an empty string
the second solution is to concatenate the string and the variable using the + operator, but this is not recommended as it can lead to errors if the variable is not a string
"""

print("Hello,", name, sep="")
print("Hello, ", name, sep="")
print("Hello, " + name)