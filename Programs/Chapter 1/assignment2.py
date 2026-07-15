# Question : Take diameter of circle as input from user and calculate area of circle. 

diameter = input("Enter the diameter of circle : ")
radius = int(diameter) / 2
area = 3.14 * (radius ** 2)
print("Radius of circle is : ", radius)
print("The area of circle is : ", area)