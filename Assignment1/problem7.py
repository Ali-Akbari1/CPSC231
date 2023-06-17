
# import random module
import random

# initialize player and computer score
playerScore = 0
computerScore = 0

# player function
def playerturn():

    # initialize variables and make player score a global variable
    global playerScore
    turnScore = 0
    totalScore = playerScore

    # while loop to simulate rolls
    while True:

        # asks user for choice whether they want to roll or hold
        choice = input("Would you like to (r)oll or (h)old ")

        # if user chooses roll dice is rolled
        if choice == "r":

            # roll the dice
            rollValue = random.randint(1, 6)
            print(f"Player rolled a {rollValue}")

            # if the user rolled a 1 they pigged out and break out of loop
            # their turn score is set to 0
            if rollValue == 1:
                turnScore = 0
                print("Pigged out! \n")
                break

            # add roll value to turn score
            else:
                turnScore += rollValue

            # if the players score reaches over 100 the game stops
            if playerScore + turnScore >= 100:
                break

        # if the player chooses to hold then add current turn score to player score
        elif choice == "h":
            playerScore += turnScore
            break

    # print turn score player score and computer score
    # update total score and player score
    print(f"Total Turn score = {turnScore} \n")
    totalScore += turnScore
    playerScore = totalScore
    print(f"Player's Score: {playerScore}")
    print(f"Computer's Score: {computerScore} \n")

    # if player score is over 100 print the winning messages
    if playerScore >= 100:
        print(f"Final Score Player: {playerScore} vs. Computer: {computerScore}")
        print("Player Wins!")

# computer turn function
def computerturn():

    # initialize variables and make computer score a global variable
    global computerScore
    turnScore = 0
    totalScore = computerScore

    while True:

        # break out of loop if turnScore is greater than 100
        if turnScore >= 20:
            break

        # roll the dice
        rollValue = random.randint(1, 6)
        print(f"Computer rolled a {rollValue}")

        # if the user rolled a 1 they pigged out and break out of loop
        # their turn score is set to 0
        if rollValue == 1:
            turnScore = 0
            print("Pigged out!")
            break

        # add roll value to turn score
        else:
            turnScore += rollValue

        # if the computers score reaches over 100 the game stops
        if computerScore + turnScore >= 100:
            break

    # print turn score player score and computer score
    # update total score and computer score
    print(f"Total Turn score = {turnScore} \n")
    totalScore += turnScore
    computerScore = totalScore
    print(f"Player's Score: {playerScore}")
    print(f"Computer's Score: {computerScore} \n")

    # if computer score is over 100 print the winning messages
    if computerScore >= 100:
        print(f"Final Score Player: {playerScore} vs. Computer: {computerScore}")
        print("Computer Wins!")


# main function
def main():
    global playerScore
    global computerScore

    print(f"Player Score: {playerScore}")
    print(f"Computer Score: {computerScore} \n")

    # make player turn random by choosing between 1 and 2
    playerTurn = random.randint(1, 2)

    # main game while loop before player or computer scores reach 100
    while playerScore < 100 and computerScore < 100:

        # if player turn variable returned 1 player
        # starts and that function is started
        # after the players turn it switches to computers turn
        if playerTurn == 1:
            print(f"It's Player turn")
            playerturn()
            playerTurn = 2

        # computers turn
        else:
            print(f"It's Computers turn")
            computerturn()
            playerTurn = 1


main()
