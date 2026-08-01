# "with" keyword will automatically close the file, no need to close the file
file = open("report.txt", "r")

with open("report.txt", "r") as f:
    # data = f.read()
    # print("File Data: ", data)

    # readline() method
    # line1 = f.readline()
    # line2 = f.readline()
    # print("Line 1", line1)
    # print("Line 2", line2)

    # read_lines method
    read_lines_methods = f.readlines()
    print(read_lines_methods)