# Functions are a collection of code that perform a certain task. Functions help organize, and break down code into
# smaller more manageable chunks.

def say_hi():  # Initializing and naming the function.
    print("Hello, user.")  # All code that will be recognized inside the function needs to be indented.


# Calling the function.

print("Top code.")
say_hi()  # This is how you call the function.
print("Bottom code.\n")


# Parameters are pieces of information given to the function.

def say_bye(name):  # 'name' is the parameter the function needs, and will replace into the code it executes.
    print("Goodbye, " + name)


say_bye("John")  # "John" is the name that will be given to the parameter 'name'.


def hi_name_age(name, age):  # Functions can have multiple parameters.
    print("Hello, " + name + ". You are " + str(age) + " years old.")


hi_name_age("Cyle", 32)
