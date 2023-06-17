# write a function named sum_digits that takes an integer as an argument
# calculate the sum of its individual digits
# and returns the sum

# for Example:
#   if we enter 231, then the sum of digits are 6
# Hint: 231 % 10 -> 1
# Hint: 231 // 10 -> 23
# Parameter: An integer which the sum-digits is being calculated
# Returns: an integer which is the sum of its digits

def sum_digits(n):
    result = 0
    while n != 0:
        result = result + (n % 10)
        n = n // 10
    return result


def main():
    n = int(input("Enter a non negative integer: "))
    print("Sum of the digits is:", sum_digits(n))


main()


