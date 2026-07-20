# dictionary
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "city": "New York",
    "name": "Jane"  # Duplicate key, will overwrite the previous value
}

print("Type of student:", type(student)) 

# Accessing value using key
print(student["name"])  

# Length of the dictionary
print(len(student))  

# update the city of the student
student["city"] = "Los Angeles"
print("Updated city:", student["city"])
print("Updated student dictionary:", student)

# add a new key-value pair to the dictionary
student["country"] = "USA"
print("Updated student dictionary:", student)

# remove a key-value pair from the dictionary
student.pop("country")
print("Updated student dictionary:", student)

# print the keys of the dictionary
print("Keys of student dictionary:", student.keys())

# print the values of the dictionary
print("Values of student dictionary:", student.values())

# print all items
print("Items of student dictionary:", student.items())
