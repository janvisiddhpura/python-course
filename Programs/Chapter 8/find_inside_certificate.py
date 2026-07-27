# A program to read a text from a given file certificate.txt
# find whether it contains the word live.

file = open("certificate.txt", "r")
data_file = file.read()

data_file = data_file.lower()

if "live" in data_file:
    print("Yes, Live word is present in the file")
else:
    print("No")