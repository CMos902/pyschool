name = "Cyle"
age = 32
# Changing the below bool variables will change the output of this program.
is_human = True
is_tall = False

if is_human and is_tall:  # Checks is_human AND is_tall is True. If not, move to the next statement.
    print(name + " is human and tall")
elif is_human and not is_tall:  # 'not is_tall' will flip the bool value for 'is_tall'.
    print(name + " is human and not tall.")
elif is_human or is_tall:  # Checks is_human OR is_tall is True. If not, move to the next statement.
    print(name + " is a human or tall.")
else:  # If neither of the above statements are True, Python will run the else statement.
    print(name + " is not human or tall.")
