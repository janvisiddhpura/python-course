def introduce(name, age):
    print("Name:", name, "Age:", age)

# it'll produce an bug like name and age both values will be swaped
# thus, keyword arguments can be used
# introduce(28, "Jack")
introduce(age = 28, name = "Jack")

"""
# TypeError: introduce() got multiple values for argument 'name'
introduce(28, name = "Jack")
# SyntaxError: positional argument follows keyword argument
introduce(age = 28, "Jack")
"""