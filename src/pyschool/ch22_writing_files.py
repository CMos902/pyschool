
# This will append new information to the chosen file. Appending is adding to the end.
employee_file = open("/Users/cylem/IdeaProjects/pyschool/data/employees.txt", "a")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

# This will overwrite the entire contents of the file with whatever is passed to `write()`.
# employee_file = open("/Users/cylem/IdeaProjects/pyschool/data/employees.txt", "w")  <--- Notice the "w"
# employee_file.write("\nKelly - Customer Service")
# employee_file.close()

# New files cna be created using as well.
employee_file1 = open("/Users/cylem/IdeaProjects/pyschool/data/employees1.txt", "w")
employee_file1.write("\nKelly - Customer Service")
employee_file1.close()
