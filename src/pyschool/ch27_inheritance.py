from Chef import Chef
from Chef_Chinese import ChineseChef

# Chef is a regular chef who can make simple dishes (chicken, salad, desert). See Chef.py

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()
print()

# To have a specialty chef can make everything a regular chef can, plus some.

# Let's make a specialty chef and they will inherit the Chef class. See Chef_Chinese.py

# Now let's try the ChineseChef class that inherited the Chef class. Don't forget to import.

myChineseChef = ChineseChef()
myChineseChef.make_salad()
myChineseChef.make_sushi()
myChineseChef.make_special_dish()

# But wait! The chinese chef's special dish isn't BBQ ribs. Go back to Chef_Chinese.py to fix it.
