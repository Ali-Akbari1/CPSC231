
# import random module
import random

# set turn score and total score to 0
turnScore = 0
totalScore = 0

# while current score is less than 100 and turn score is less than 20
while totalScore < 100:
    while turnScore < 20:

        # roll the dice
        rollValue = random.randint(1, 6)

        print(f"You rolled a {rollValue}")

        # if the user rolled a 1 they pigged out and break out of loop
        # their turn score is set to 0 and their total score is reset
        if rollValue == 1:
            totalScore -= turnScore
            turnScore = 0
            print("Pigged out!")
            break

        # add roll value to total score and turn score
        else:
            totalScore += rollValue
            turnScore += rollValue

            # break out of the loop if total score reaches over 100
            if totalScore >= 100:
                break

    # print total score and turn score after every turn then reset turn score
    print(f"Turn score = {turnScore}")
    print(f"New total score = {totalScore}")
    turnScore = 0

