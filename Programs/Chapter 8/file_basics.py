# import os

# print(os.getcwd())    # print present working directory

file = open("sample.txt", "r") # default read mode if param not provided
data_file = file.read()

print("Data of the file is:", data_file)