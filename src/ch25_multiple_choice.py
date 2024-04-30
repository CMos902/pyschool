from Prompts import Prompts

# This is a simple multiple choice quiz that will most of the things learned in previous chapters.

# First we'll set up the prompts that the user will see. They will be stored in an array for easy access.
prompts = [
    "What color are apples?\n(a) Red\n(b) Blue\n(c) Orange\n",
    "What color are bananas?\n(a) Red\n(b) Yellow\n(c) Orange\n",
    "What color are blueberries?\n(a) Red\n(b) Yellow\n(c) Blue\n",
]

# Now that we have the prompts, lets make a question class in a new module. Look for question.py.
# Don't forget to import the class!

# Setting up the array of questions and  their correct answer.
questions_and_answers = [
    Prompts(prompts[0], "a"),
    Prompts(prompts[1], "b"),
    Prompts(prompts[2], "c")
]

# Create the function to print each prompt individually and keep track if the user answered correctly.


def run_test(questions):
    score = 0
    for question in questions:  # As we can see here, these names are horrible. Maybe I'll fix this later.
        print(question.question)
        answer = input("Your answer: ")
        print()
        if answer == question.answer:
            score += 1
    print("Your scored " + str(score) + " out of " + str(len(questions)) + ".")


# Finally, call the run_test function to take the test.
run_test(questions_and_answers)
