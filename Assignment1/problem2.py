
# import random module
import random

# variable total number of rolls
total = 0

# number of rolls user wants to simulate
numOfRolls = int(input("Enter the amount of simulated rolls "))
print(f"Rolling {numOfRolls} times...")

# for loop to loop through all rolls
for i in range(1, numOfRolls + 1):
    rollValue = random.randint(1, 6)

    # add roll value to total
    total += rollValue

# get the average by dividing total value divide number of rolls
# then print the average
average = total/numOfRolls
print(f"Estimated expectation: {average} ")


