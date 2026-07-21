# sum of n natural numbers
n = int(input("Enter the range: "))
num = n
sum = 0
while n >= 1:
    sum = sum + n
    n = n - 1
print(f"Sum of {num} natural number: {sum}", num, sum)