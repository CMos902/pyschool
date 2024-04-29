num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
decimal_num1 = input("Enter a decimal number: ")
decimal_num2 = input("Enter another decimal number: ")
# Got the user inputs, but Python declared them as strings.
print("DEBUG: num1 type:", type(num1), "; num2 type:", type(num2))

result = num1 + num2
print("Unexpected result:", result)  # Because the variables are string, the output won't be as expected.

# Convert strings the integers.

result = int(num1) + int(num2)  # Change num1 and num2 from str to int to get the expected result.
print("Expected result:", result)

# Convert strings to floats.

result = float(decimal_num1) + float(decimal_num2)  # Using floats will let the user enter any number, whole or decimal.
print("Float result: ", result)  # <class 'float'>
