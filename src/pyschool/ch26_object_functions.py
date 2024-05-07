
from Students_2 import Student

# Class functions are functions used inside a class to modify get specific information about the class.
# In Student_2.py there is a Student class.

# Here are some student objects created from that class.
student_1 = Student("Jill", "Finance", 3.1)
student_2 = Student("Albert", "Physics", 4.0)

# Move over to Students_2.py to see the function inside a class.

# The class has a function that we can use to see if the student is on the honor roll. Try it out.

print(student_1.on_honor_roll())
print(student_2.on_honor_roll())
