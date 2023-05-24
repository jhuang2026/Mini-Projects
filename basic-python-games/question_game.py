# This game asks the users a bunch of questions, and if they answer these questions correctly, their score increases
# The goal is to get all the questions correctly

print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

# Checks if the user's input is in the order y-e-s, and quits if it's not
if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

if score == 1:
    print("You got", score, "question correct!")
else: 
    print("You got", score, "questions correct!")

# Prints the score of the user as a percentage based on the 4 questions
print("You got " + str((score/4) * 100) + "%")