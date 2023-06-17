
# import random module
import random

# initialize player one and two score
playerOneScore = 0
playerTwoScore = 0


# function to simulate player ones turn
def playeroneturn():

    # initialize variables and make player one score global variable
    global playerOneScore
    turnScore = 0
    totalScore = playerOneScore

    # while loop to simulate rolls
    while True:

        # break out of loop if turnScore is greater than 100
        if turnScore >= 20:
            break

        # roll dice
        rollValue = random.randint(1, 6)
        print(f"Player One rolled a {rollValue}")

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
        if playerOneScore + turnScore >= 100:
            break

    # print turn score player one score and player two score
    # update total score and player score
    print(f"Total Turn score = {turnScore} \n")
    totalScore += turnScore
    playerOneScore = totalScore
    print(f"Player One's Score: {totalScore}")
    print(f"Player Two's Score: {playerTwoScore} \n")

    # if player score is over 100 print the winning messages
    if playerOneScore >= 100:
        print(f"Final Score Player One: {playerOneScore} vs. Player Two: {playerTwoScore}")
        print("Player One Wins!")


# function to simulate player twos turn
def playertwoturn():

    # initialize variables and make player two score global variable
    global playerTwoScore
    turnScore = 0
    totalScore = playerTwoScore

    # while loop to simulate rolls
    while True:

        # break out of loop if turnScore is greater than 100
        if turnScore >= 20:
            break

        # roll the dice
        rollValue = random.randint(1, 6)
        print(f"Player Two rolled a {rollValue}")

        # if the user rolled a 1 they pigged out and break out of loop
        # their turn score is set to 0
        if rollValue == 1:
            turnScore = 0
            print("Pigged out!")
            break

        # add roll value to turn score
        else:
            turnScore += rollValue

        # if the players score reaches over 100 the game stops
        if playerTwoScore + turnScore >= 100:
            break

    # print turn score player one score and player two score
    # update total score and player score
    print(f"Total Turn score = {turnScore} \n")
    totalScore += turnScore
    playerTwoScore = totalScore
    print(f"Player One's Score: {playerOneScore}")
    print(f"Player Two's Score: {totalScore} \n")

    # if player score is over 100 print the winning messages
    if playerTwoScore >= 100:
        print(f"Final Score Player One: {playerOneScore} vs. Player Two: {playerTwoScore}")
        print("Player Two Wins!")

#main function
def main():
    global playerOneScore
    global playerTwoScore

    print(f"Player One's Score: {playerOneScore}")
    print(f"Player Two's Score: {playerTwoScore} \n")

    # make player turn random by choosing between 1 and 2
    playerTurn = random.randint(1, 2)

    # main game while loop before player scores reach 100
    while playerOneScore < 100 and playerTwoScore < 100:

        # if player turn variable returned 1 player
        # one starts and that function is started
        # after player ones turn it switches to player 2
        if playerTurn == 1:
            print("It's Player One's turn")
            playeroneturn()
            playerTurn = 2

        # player two's turn
        else:
            print("It's Player Two's turn")
            playertwoturn()
            playerTurn = 1


main()
