
# When reading a file, it first needs to be opened. Use `open("(file name or directory path)")` as the first parameter.
# The second parameter of `open()` is the mode that the file will be opened as.
# "r" = read-only, "w" = write, "a" = append, "r+" = read and write

employee_file = open("/Users/cylem/IdeaProjects/pyschool/data/employees.txt", "r")

# Checking if a file is readable.
# print(employee_file.readable())  # Returns a boolean value.
# print()

# Prints all the contents of the file.
# print(employee_file.read())
# print()

# Prints a line from a file. Running this statement again will print the next line of the file.
# print(employee_file.readline())
# print()

# The function `readlines` puts all the file's lines in a list.
# print(employee_file.readlines())

# Prints the first line of the file.
# print(employee_file.readlines()[1])
# print()

# Prints each line of the file.
for employee in employee_file.readlines():
    print(employee)

employee_file.close()  # ABC - Always Be CLosing
