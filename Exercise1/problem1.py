# Ali Akbari ID #: 30171539

# main function
def main():

    # get the number of sides from the user
    numOfSides = int(input("Please enter the number of sides of your shape from Assignment3-10 "))

    # check if input is in correct range
    if numOfSides < 3 or numOfSides > 10:
        print("That is not a value between Assignment3-10")
        main()

    # check number of sides and print the shape
    elif numOfSides == 3:
        shape = "Triangle"
        print(f"Your shape is a {shape}")

    elif numOfSides == 4:
        shape = "Square"
        print(f"Your shape is a {shape}")

    elif numOfSides == 5:
        shape = "Pentagon"
        print(f"Your shape is a {shape}")

    elif numOfSides == 6:
        shape = "Hexagon"
        print(f"Your shape is a {shape}")

    elif numOfSides == 7:
        shape = "Heptagon"
        print(f"Your shape is a {shape}")

    elif numOfSides == 8:
        shape = "Octagon"
        print(f"Your shape is a {shape}")

    elif numOfSides == 9:
        shape = "Nonagon"
        print(f"Your shape is a {shape}")

    elif numOfSides == 10:
        shape = "Decagon"
        print(f"Your shape is a {shape}")


main()
