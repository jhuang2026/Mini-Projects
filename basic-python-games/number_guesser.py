# This game generates a random number, and we track how many attempts it takes for the user to guess the number
# The goal is to guess the number with the least amount of guesses

import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

# We select a number between 0 and top_of_range (inclusive)
random_number = random.randint(0, top_of_range)
# Tracks the number of guesses the user has made
guesses = 0

print("We have selected a number between 0 and your inputted number!")

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number instead.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Your guess is greater that the number!")
    else:
        print("Your guess is below the number!")

print("You got it in", guesses, "guesses")
