# You could just copy-paste the Chef class over here, since the Chinese chef can do everything a regular chef can. That
# can be a lot of work, so lets try inheriting.

from Chef import Chef  # First, from Chef.py, import the Chef class.


class ChineseChef(Chef):
    # Notice the parameter passed to the class. Now ChineseChef can do everything Chef can.

    def make_sushi(self):
        print("Sushi has been made")

    # Move back to ch27 and try it out.

    # The chinese chef's special dish is orange chicken, not BBQ ribs. To fix this, simply override the
    # make_special_dish function by writing again to match the chinese chef.

    def make_special_dish(self):
        print("Orange chicken dish has been made")
