numLetters = 0
for letters in "Pyschool":
    print(letters)
    numLetters += 1
print("The number of letters in this string are: " + str(numLetters))
print()

people = ["Aaron", "Becky", "Charlie"]
for names in people:
    print(names)
print()

for index in range(10):  # Prints the range of numbers [0 - 10). (10 not included)
    print(index)
print()

for index_two in range(3, 10):  # Prints the range of numbers [3 - 10). (10 not included)
    print(index_two)
print()

for index_three in range(5):
    if index_three == 0:
        print("first iteration")
    else:
        print("not first")
