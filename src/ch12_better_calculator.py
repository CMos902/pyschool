"""
When getting a user input, Python initializes the input as a string by default. For this program, the user will be asked
as enter a number, and we want Python the store that value as a float, not a string. The code below does that. This will
cause an error is the user enters anything other than a number. Maybe, we cna come back to that later. If I remember.
"""
# TODO: Add error handling for invalid input for num1 and num2.
# TODO: Config output to match variable type input for num1 and num2.

num1 = float(input("Enter first number: "))
operator = (input("Enter operator: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
else:
    print("Invalid operator.")
