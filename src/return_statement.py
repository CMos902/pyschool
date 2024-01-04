# Return statements get information back from a function.

def cube(num):  # Initializing the function.
    return pow(int(num), 3)  # This is our return statement.
    # "pow(int(num), 3)" This expression uses the pow function to raise num to the power of 3.
    # "int(num)" converts the input num to an integer, ensuring it's a numerical value.
    # Once the calculation is done, the solution is returned to whatever called the function. (print statement below)


print(cube(input("Enter a number: ")))  # Prompts the user for a number, and prints the return statement.

# Another initialize a variable with the function. See below:


def to_the_fourth(num):
    return int(num) * int(num) * int(num) * int(num)  # A little different math.


result = to_the_fourth(input("x^4 = ? Enter a number for x: "))
print(result)

# Note: The return statement works as a break, so any code after a return in a function, won't be recognized.
