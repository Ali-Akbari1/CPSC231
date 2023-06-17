
# import random module
import random

# set turn score variable to 0
turnScore = 0

# while loop to keep rolling until the turn score hits 20
while turnScore < 20:

    # rolling the dice
    rollValue = random.randint(1, 6)

    # print what the user rolled
    print(f"You rolled a {rollValue}")

    # if the user rolled a 1 they pigged out and their turn score is set to 0
    if rollValue == 1:
        turnScore = 0
        print("Pigged out!")

        # break out of the loop
        break

    # add rollvalue to turn score if they rolled anything other than a 1
    else:
        turnScore += rollValue

# print the users turn score
print(f"Turn score = {turnScore}")

