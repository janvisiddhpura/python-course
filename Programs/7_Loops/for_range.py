# for loop range

for item in range(2, 20, 2):
    print(item, end=", ")
    # 2, 4, 6, 8, 10, 12, 14, 16, 18

print ("\n")
print(*range(20, 101, 20), sep= ", ")
    # 20, 40, 60, 80, 100