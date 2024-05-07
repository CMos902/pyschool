
# Classes are a way to define a data type.

# For example, there is no data in Python that represents a student. So we will have to create one.
# Let's create a student class.

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
# From here, check out the module Student.py
