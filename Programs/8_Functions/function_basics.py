# # function basics

# # PROBLEM: repetition of same code

# # sum of 2 numbers
# a = 5
# b = 4
# sum = a + b
# print(sum)

# # some more lines
# average = (a+b)/2
# print(average)

# # after .. 1000 lines of code
# # again sum of 2 numbers

# SOLUTION: use user defined function
def sum():
    a = 99
    b = 1
    sum = a + b
    print(sum)

print("Hello from Python!!")
print("Let's call the function 1st time!")
sum()
print("Let's call the function 2nd time!")
sum()
print("Let's call the function 3rd time!")
sum()
print("Thus, we can reuse the same code as many times as we want by calling that function!")