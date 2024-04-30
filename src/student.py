
from ch24_classes_and_objects import Student

student1 = Student("Cyle", "CIS", 4.0, False)

# This creates the object `student1`. That object has multiple variables that need to be assigned.
# In the line about student1 is assigned a name. student1.name = "Cyle".
# It is also given a major, gpa, and told if it's on probation (or not).
# student1.major = CIS, student1.gpa = 4.0, student1.is_on_probation = False
# Now these characteristics of student1 can be called on.

print(student1.name, student1.major, student1.gpa, student1.is_on_probation)

# Using the same class, we can create as many objects as we need to define students.
student2 = Student("Billy", "Biology", 3.2, False)
if student2.is_on_probation:
    print("uh oh, " + student2.name + ". you are on probation")
else:
    print("nice, " + student2.name + ". you are not on probation")
