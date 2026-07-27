# Open a file called report.txt in write mode.
# ifthe files doesn't exist, it'll create it.

file = open("write_mode_sample.txt", "a")
# Use append mode if don't want to override the content of the file
file.write("Learning Python in a detailed way! That's Great!!")