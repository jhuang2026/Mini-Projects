# This games simulates a real rock, paper, scissors game, and it also keeps track of scores.

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

print("Let's play rock, paper, scissors!")

while True:
    user_input = input("Type Rock/Paper/Scissors of Q to quit: ").lower()
    if user_input == 'q':
        break

    # If the user's input isn't one of the 3 possible words, we go back to line 11 
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # In this case, rock: 0, paper: 1, scissor: 2
    computer_pick = options[random_number]
    print("Computer picked:", computer_pick)

    if user_input == computer_pick:
        print("You tied!")
        continue

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else: 
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")

if user_wins > computer_wins:
    print("\nYour The Winner!")
elif computer_wins > user_wins:
    print("\nThe Computer Wins!")
else:
    print("\nIt's a Tie!")
