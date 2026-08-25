# keyword variable length arguments - **kwargs
# *kwargs = take all the args and put in a dict
def create_user(**details):
    print(type(details))
    print(details)

create_user(name = ["Jack", "Oggy"], age = [27, 29], city = ["NY", "WA"])

# TypeError: create_user() takes 0 positional arguments but 3 were given
# need to provide named inputs
# create_user("Jack", 99, "NY")

# TypeError: create_user() takes 0 positional arguments but 1 was given
# need to provide multiple arguments
# create_user("Bob")

# NORMAL PARAMs: FIXED INPUTS
# *ARGS: UNLIMITED UNNAMED INPUTS
# **KWARGS: UNLIMITED NAMED INPUTS