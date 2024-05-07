# Try-except blocks handle errors (exceptions) that may occur during a program's execution. They provide a controlled
# way to manage these errors and prevent your program from crashing unexpectedly.

# The code that may be susceptible to errors should be within the try block.
try:
    number = int(input("Enter a number: "))
    print(number)

# The exception block defines how to handle the error if it occurs.
except ValueError:
    print("Invalid input")

else:  # (optional)
    print("This code will execute if there are no exceptions.")

finally:  # (optional)
    print("Code in the block will execute regardless if exceptions occur or not.")
