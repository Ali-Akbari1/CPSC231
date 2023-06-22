# Ali Akbari 30171539

# Import Random Module
import random

# Open lexicon file
f = open("cpsc231-lexicon.txt", "r")

# Initialize validWords and secretWord list
validWords = []
secretWord = []

# Read lines from file
lines = f.readlines()

# Close the file
f.close()

# Add words to validWords list that are greater than or equal to 4
for word in lines:
    if len(word) > 4:
        validWords.append(word.rstrip())

# Initialize secretWord and wordLength variables
secretWord = list((random.choice(validWords)))
wordLength = len(secretWord)

# Initialize the guess list
guessList = ["- "] * wordLength


# Game function
def game():
    # Initialize a list for guessed letters and bad guesses
    numOfGuesses = 8
    guessedLetters = []
    badGuesses = []

    # Print starting game board
    print("Hello welcome to Hangman! I will be thinking of a secret word. \n"
          "To win You have to guess the word I am thinking of! \n"
          "You can guess my secret word by choosing letters \n"
          "You start with 8 guesses and for every wrong letter, you will lose a guess \n"
          "You are not allowed to choose the same letter twice!\n"
          "Lets Begin! \n ")

    print("The secret word looks like: \n", *guessList)

    # Main game loop
    while numOfGuesses > 0:

        print(f"You have {numOfGuesses} guesses remaining ")

        # Get the guess from the user
        guess = input("What is your next guess: ")

        # If user already guessed the letter repeat loop
        if guess in guessedLetters:
            print("Please guess a letter you have not guessed already")
            continue

        # If user guessed correctly
        if guess in secretWord:
            print("Nice guess!")
            print("Bad Guesses:", *badGuesses)
            guessedLetters.append(guess)
            for i in range(wordLength):
                if secretWord[i] == guess:
                    guessList[i] = guess

        # If user did not guess correctly
        else:
            numOfGuesses -= 1
            print(f"Sorry there is no '{guess}'")
            guessedLetters.append(guess)
            badGuesses.append(guess)
            print("Bad Guesses:", *badGuesses)

        # Printing game board
        print(*guessList)

        # If the users guess list and the secret word list are equivalent
        # Then the user has won the game and break out of the game loop
        if guessList == secretWord:
            print("You Won! Congratulations")
            break

        # If the user has no more guesses left they lost the game
        # And break out of the game loop
        if numOfGuesses <= 0:
            print("Sorry you lost, no more guesses left")
            break

    # At the end of the game either win or loss print the secret word
    print(f"The word was ", *secretWord)


game()
