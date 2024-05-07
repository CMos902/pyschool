class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    # self refers to the student object being referenced.
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    # Move back to ch26.
