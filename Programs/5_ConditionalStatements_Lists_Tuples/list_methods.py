# list methods

# indexing
marks = [90, 100, 99, 83]
print("First 2 elements of marks:", marks[0:2])
marks[1] = 95  # changing the value of 2nd element
print("Updated marks:", marks)

# prints the minimum value in the list
print(min(marks))  

# prints the maximum value in the list
print(max(marks))  

# strings are immutable, but lists are mutable
# name = "Alice"
# name[1] = "l"  # this will raise an error because strings are immutable
# print("Updated name:", name)  # this line will not be executed

# slicing
print("Elements from index 1 to 3:", marks[1:3])

# other methods

# adds 88 to the end of the list
marks.append(88)  
print("Marks after appending 88:", marks)

# sort
marks.sort()
print("Marks after sorting:", marks)

# reverse
marks.reverse() 
print("Marks after reversing:", marks)

# inserts 92 at index 2
marks.insert(2, 92)  
print("Marks after inserting 92 at index 2:", marks)

# removes the first occurrence of 90
marks.remove(90)  
print("Marks after removing 90:", marks)