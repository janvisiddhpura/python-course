# 2 arguments
def add(a, b):
    return a + b

print(add(10, 20))

# 3 arguments
def add(a, b, c):
    return a + b + c

print(add(10, 20, 30))

# *args = take all the args and put in a tuple
# it'll only take positional arguments, not keyword args.
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add(10, 20, 30, 40, 50, 60))