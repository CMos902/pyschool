# Tuples are a type of data structure. Basically, a container where we can store values. Similar to lists.
# There are some key differences though.
# To create a tuple, use () after a variable (see line 5).

coord = (4, 5)  # Initializing coord tuple.

# Tuples are immutable, meaning they CANNOT be changed from there initiated value.
# Tuples are indexed just like anything else in Python, starting at 0.

print(coord[0])  # Print index 0

# If we try to run 'coord[0] = 1', Python would show an error because tuples are immutable.

# Creating a list of tuples.

coord_lists = [(1, 2), (3, 4), (5, 6)]  # A list of tuples.
# Tuples can be added, removed, or moved around the list; but the values of the tuple can't be altered.
