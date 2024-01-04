# When Python [], it knows a list is being initiated.
# Lists can store multiple inputs at once (str, int, bool).
# ex. list = ["String", 2023, True].
# Each item in the list is assigned an index.

people = ["Aaron", "Brittanie", "Charlie", "Dianne", "Eric"]  # A list of strings.
# index =    0          1           2          3        4

print(people)  # Prints this list 'people'.
print(people[2])  # Prints index 2 from list 'people'.
print(people[-1])  # Prints last index from list 'people'. [-2] would be the second to last index and so on.
print(people[1:])  # Prints all the entire list starting from index 1.
print(people[1:3])  # Prints index's 1-3 from list 'people'.

# Modifying lists.

people[1] = "Brenda"  # Modifies index 1.
print(people)

# List Functions

numbers = [2, 6, 7, 13, 38]

people.extend(numbers)  # Add 'numbers' list to the end of 'people' list.
print(people)

people.append(42)  # Adds an index to the end of list 'people'. In this case it added the int '42'.
print(people)

people.insert(1, "Barbie")  # Inserts Barbie into index 2, and shifts all of index's up.
print(people)

people.remove("Aaron")  # Removes Aaron from the list.
print(people)

people.clear()  # Completely empties the list.
print(people)

numbers.pop()  # Removes the last index from the list.
print(numbers)

print(numbers.index(13))  # Prints the index where int 13 is located.

numbers.append(13)

print(numbers.count(13))  # Prints how many times '13' appears in the list 'numbers'.

numbers.sort()  # Sorts the list in numerical/alphabetical order.

numbers.reverse()  # Reverses a lists current order.

numbers2 = numbers.copy()  # Copies the contents of numbers to numbers2.

