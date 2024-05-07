def max_num(num1, num2, num3):  # Creating a fun that will tell us the largest number passed to it.
    if num1 >= num2 and num1 >= num3:  # If num1 >= num2 AND num3, num1 will be returned.
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 4, 5))  # `max_num` is being called in a print statement, and returns the ints being passed to it.

"""
Different variables can be compared in different ways.
e.g., "String" == "String"; num1 != num2; bool1 == bool2
"""
