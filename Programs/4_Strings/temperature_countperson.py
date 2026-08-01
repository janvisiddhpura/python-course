# take input celcius from user 
# print farenheit equivalent of celcius

celcius = float(input("Enter temperature in Celsius: "))
farenheit = (celcius * 9/5) + 32
print("Farenheit value is :", farenheit)

# take input total and friends count from user
# calculate amount per person

total_bill = float(input("Enter total bill amount: "))
friends_count = int(input("Enter number of friends: "))

amount_per_person = total_bill / friends_count
print("Amount per person is :", amount_per_person)

# predict the output of the following code snippet

x = 5
y = 2.0
print(x // y)
print(x ** y)

# identify the error in the following code snippet

# if = 10     
# print(if)
# the code has a syntax error because 'if' is a reserved keyword in Python and cannot be used as a variable name.