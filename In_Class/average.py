# Compute the average of a collection of values entered by the user
# The user will enter 0 to indicate the end of the input

#initialize count and total to 0

count = 0
total = 0

value = int(input("What value do you want to enter "))

while value != 0:
    total = total + value
    count = count + 1

    value = int(input("Enter another number "))

if count == 0:
    print("No value entered by the user")

else:
    average = total/count
    print(f"The average of those numbers is {average}")
