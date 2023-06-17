# Ali Akbari ID #: 30171539

# main function
def main():

    # human years age
    age = int(input("Enter an age in human years "))

    # loop that keeps running until user inputs an age less than 0
    while age >= 0:

        # for ages from 1-2
        if age <= 2:
            age = age*10.5
            print(f"That's equivalent to {age} dog years")
            main()

        # calculate ages after 2 year
        else:
            ageAfterTwo = age - 2
            ageAfterTwo = ageAfterTwo*4
            age = 21 + ageAfterTwo
            print(f"Thats equivalent to {age} dog years")
            main()
        break




main()