"""
try = try to run the exceptional code
except = runs when exception occurs
else = runs if there is no exception
finally = always runs
"""

try:
    x = int(input("Enter number: "))
    result = 10/x

except ZeroDivisionError:
    print("You can't divide with zero!")

except ValueError:
    print("Provide right value!")

except TypeError:
    print("You can't divide with string!")

else:
    print("Result: ", result)

finally:
    print("Thanks for entering!")