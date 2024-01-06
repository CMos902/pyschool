"""
Game where a user guesses a random number until they guess correctly. But, they only have 3 attempts.
"""
import random  # Import `random` module.

secret_num = random.randrange(1, 10)  # Assign a random number 1-10 to `secret_number`
guess = ""
num_guess = 0

print("DEBUG: secret_num = " + str(secret_num))  # Just for debugging. Comment this line out to play for real.
while guess != secret_num:  # Loop that runs until the `secret_number` is guessed.
    guess = input("Guess a number 1-10: ")
    num_guess += 1  # Track the number of guesses made.
    if guess == str(secret_num):  # Win condition.
        print("Good job, you guessed correctly!")
        break  # Breaks the loop.
    elif num_guess == 3:  # Lose condition.
        print("You're out of guesses, better luck next time!")
        break
    else:
        if num_guess < 2:  # Wrong guess, but a number of guesses still left.
            print(str(3 - num_guess) + " more guesses. Try again!")
        elif num_guess == 2:  # Last guess.
            print("Last chance! Make it count.")
