# multiplication table in format like..
# 3 x 1 = 3
# 3 x 2 = 6
# .
# .
# .
# 3 x 10 = 30


n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1