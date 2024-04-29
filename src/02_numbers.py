print(2)  # Print an integer.
print(2.22)  # Print a float. By default, Python declares decimals as floats.
print(-2)  # Print a negative number

# Arithmatic.

print(3 - 4.13)  # Basic addition(+), subtraction(-), multiplication(*), and division(/).
print(3 * (5 - 3))  # Python follows standard order of operations (PEMDAS).
print(10 % 3)  # '%' is the modulus operator. The modulus divides the equation, and outputs the remainder.

# Arithmatic operators.

# + (addition)  1 + 1 = 2
# - (subtraction) 1 - 1 = 0
# * (multiplication) 2 * 2 = 4
# / (division) - Performs floating-point division by default. Use // for floor division. 10 / 3 = 3.33333; 10 // 3 = 3
# % (modulo) - Returns the remainder after division. 10 % 3 = 1
# ** (exponentiation) - Raises the left operand to the power of the right operand. 2**3 == 2^3 = 8

# Comparison Operator

# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
# is (checks object identity) - Use with caution, preference is for == for value

# Numbers can be stored to variables just like strings.

whole_number = 4  # Declared as an integer.
decimal_number = 3.14159  # Float.
negative_number = -11  # Negative number.

# Numbers can be converted to strings.

print(str(whole_number))

# Math functions built into Python. There are a lot, but here are some common ones.

print(abs(negative_number))  # Prints the absolute value of a number.
print(pow(3, 2))  # Used for exponents. Two parameters can be passed to this function. (The equation will be 3^2).
print(max(whole_number, negative_number))  # This will print the largest value passed to it.
print(min(whole_number, negative_number))  # Same as max, but prints the smallest value.
print(round(decimal_number))  # Rounds a decimal, to the nearest whole number.

# Importing.
# Following PEP 8 style guide, imports should be at the top of a file.
from math import *
# This allows us to access even more math functions. Also known as a module.

print(floor(3.7))  # Prints the lowest number. Similar to rounding down.
print(ceil(3.7))  # Prints the highest number. Similar to rounding up.
print(sqrt(49))  # Prints the square root of a number.
