# print countdown before something "exciting" happens

import time

count = int(input("Enter the counter num: "))

print("Countdown Starts Now: ")

for i in range(count, 0, -1):
    print(i)
    time.sleep(1)

print("\033[1m"+"HAPPY NEW YEAR! 🎉"+"\033[0m")