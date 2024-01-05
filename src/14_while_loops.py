"""
While loops are a structure in Python that cycles through a block of code until a set condition is met.
"""

i = 1
while i <= 10:  # First, Python checks the value of `i`, is it <= 10?
    # If True, execute this code block, until False.
    print(i)
    i += 1  # i += 1 iterates i by 1. (The same as i = i + 1)

print("Yay, we did it!")  # When False, Python moves past the while loop to the next lines of code.
