
# Creating a 2D list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Print valued from a 2D calling print and the first parameter will be the index of the list you want to look in, and
# the second parameter will be the index of the element you want to print.

# Prints row 2 column 1 (count by index).
print(number_grid[2][1])
print()

# Nested for loops

# Prints each element of [number_grid].
for row in number_grid:
    print(row)
print()

# Prints each element within each element. (digits of the array within an array).
for row in number_grid:
    for column in row:
        print(column)
