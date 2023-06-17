# compute the value of n factorial using a function

# compute the factorial
#
# Parameters:
#   an integer for which the factorial is being calculated
#   returns 1 if n is negative
#   Return: factorial of number - n


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

#
# compute factorial for a number inputted by the user
#
# Parameter: None
# Return: None

def main():
    number = int(input("Enter a non negative integer: "))
    print(number, "Factorial is:", factorial(number))


# start the main function
main()

