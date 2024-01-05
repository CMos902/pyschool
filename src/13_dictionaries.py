"""
Dictionaries are structures in Python that allow us access store info in key value pairs. Key value pairs can be created
and the information stored on them can be accessed by calling on the pair from the dictionary.

Analogy: When the pair is created, the key is the word that is identified within the dictionary; and the value is
the definition of the word.

Here we will convert the month abbreviations to the full word. e.g., Jan -> January
"""

month_conversions = {  # {} are used when creating a KVPs.
    # Key: Value
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# There are two ways to access a KVP:
print(month_conversions["Sep"])  # Calling the key and printing the value.
# and
print(month_conversions.get("Oct"))

"""
When using the .get method to access the KVP it can have a default value set incase it receives an unknown key.
"""
print(month_conversions.get("Kan", "Invalid input."))
#                                   Default value

# Key don't have to be strings, and can be ints as well.
