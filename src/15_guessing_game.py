"""
Game where a user guesses a predefined number until they guess correctly. But, they only have 3 attempts.
"""
num = "10"
guess = ""
num_guess = 0
guess_left = 2 - num_guess

while guess != num:
    guess = input("Guess a number 1-10: ")
    num_guess += 1
    if num_guess == 3:
        print("You're out of guesses, better luck next time!")
        break
    elif num_guess != 3 and guess == "10":
        print("Good job, you win!")
    else:
        print(str(guess_left) + " more guesses, try again!")
