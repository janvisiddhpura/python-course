# take 5 foods from user and store them in a list, print list with its length and print each food in the list

food_list = []
food1 = input("Enter food 1: ")
food2 = input("Enter food 2: ")
food3 = input("Enter food 3: ")
food4 = input("Enter food 4: ")
food5 = input("Enter food 5: ")

food_list = [food1, food2, food3]
food_list.append(food4)
food_list.append(food5)

print("Food list:", food_list)
print("Length of food list:", len(food_list))
