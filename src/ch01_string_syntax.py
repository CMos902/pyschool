# Variables aren't declared in Python. It is a dynamically typed language.
phrase = "Hello world"  # String.

# note: '\' is an escape character which allows for typing characters that might break a code. ex: ( ) \ / " ' :

print(phrase)  # Prints variable 'phrase'.
print("")  # Print a blank line.
print(phrase + "\n")  # '\n' prints whitespace under where the line it was coded to.

# Concatenation!
print(phrase + "!")  # Combining two strings.
print(phrase + ". " + phrase + ".")

# Functions! There are way more than what I have listed below.
print(phrase.lower())  # Makes a string all lowercase.
print(phrase.upper())  # Makes a string all uppercase.
print(phrase.isupper())  # Checks if a string is all uppercase. Outputs a boolean.

# Functions can be combined!
print(phrase.upper().isupper())  # Converts phrase to uppercase, and outputs boolean true.

# String length.
print(len(phrase))  # Outputs the length of a string.

# Print a specific character in a string.
print(phrase[0])  # Remember, character index starts at 0 in Python; Java as well!
# Example: Hello
#          01234

print(phrase.index("H"))  # Outputs the index of the Letter 'H' in the string (Output will == "0").
# Passing information to a function like this gives it a value. This is commonly called 'passing a parameter'.

print(phrase.index("world"))  # This will tell us which index this part of the string 'phase' starts (Output == '6').

print(phrase.replace("Hello", "Greetings"))
