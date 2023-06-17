# Ali Akbari 30171539

# isPrime function to check if a number is a prime number
def isPrime(number):
    # if number from user is one or less it is not a prime number
    if number <= 1:
        return False
    elif number > 1:
        for i in range(2,number):
            # if remainder is 0
            if (number % i) == 0:
                return False

    return True

# main function
def main():

    # gets number from the user
    number = int(input("Enter a number to check if it is prime "))

    # if isPrime is true print the number is a prime number
    # otherwise print it is not a prime number
    if isPrime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

main()
