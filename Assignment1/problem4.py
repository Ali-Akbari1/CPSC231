
# import random module
import random

# get the current score from the user input
currentScore = int(input("Enter current score: "))

# set the turn score to 0
turnScore = 0

# while current score is less than 100 and turn score is less than 20
while currentScore < 100:
    while turnScore < 20:

        # roll dice
        rollValue = random.randint(1, 6)

        print(f"You rolled a {rollValue}")

        # if the user rolled a 1 they pigged out and break out of loop
        # their turn score is set to 0 and their current score is reset
        if rollValue == 1:
            currentScore -= turnScore
            turnScore = 0
            print("Pigged out!")
            break

        # add roll value to current score and turn score
        else:
            turnScore += rollValue
            currentScore += rollValue

        if currentScore >= 100:
            break
    break

# print users turn score and current score
print(f"Turn score = {turnScore}")
print(f"New total score = {currentScore}")