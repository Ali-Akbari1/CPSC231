# Ali Akbari 30171539

# Proper divisor function
def properdivisor(n):
    # Initialize variable divisor list
    divisorList = []

    # Loop through all numbers from 1 to the number
    for i in range(1, n):

        # If number divides evenly add it to divisor list
        if n % i == 0:
            divisorList.append(i)

    return divisorList


# Perfect integer function
def perfectinteger(n):
    listSum = 0

    # Loop through the divisor list and add the numbers
    for i in properdivisor(n):
        listSum += i

    # Return true if the sum of all the divisors is equal to the number
    if listSum == n:
        return True


# Main function
def main():

    # Get number from the user
    n = int(input("Please enter a positive integer: "))

    # Run the proper divisor function and print out the divisors
    print(f"proper divisors of {n} is {properdivisor(n)}")

    # If perfect integer returns true print it is a perfect number
    if perfectinteger(n):
        print(f"{n} is a perfect number")

    # Otherwise it is not a perfect number
    else:
        print(f"{n} is not a perfect number")


main()
