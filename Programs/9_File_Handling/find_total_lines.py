# find how many lines are present in notes.txt
with open("notes.txt", "r") as f:
    total_lines = f.readlines()
    print(total_lines)
    print("Total no. of lines:", len(total_lines))