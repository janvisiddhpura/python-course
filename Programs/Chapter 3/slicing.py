# strings slicing

str = "Gulab Jamun"

print("First 5 characters of str:", str[0:5])
print("First 5 characters of str without index:", str[:5])
print("From 6th index to 11th index of str:", str[5:11])
print("From 6th index to end of str witout index:", str[5:])

# with negative index
print("Last 5 characters of str using negative index:", str[-5:])

# print middle 3 characters of str, last 2 characters of str, first 2 characters of str
mid = len(str) // 2
print("Middle 3 characters of str:", str[mid-1:mid+2])
print("Last 3 characters of str:", str[-3:])