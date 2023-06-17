# determine the number of roots of a quadratic equation using a function

# Parameters:
#           a: the coefficient of x^2
#           b: the coefficient of x
#           c: constant
# Return: the number of roots (0,1,2)

def numroots(a, b, c):

    disc = (b**2) - (4 * a * c)
    if disc > 0:
        return 2
    elif disc == 0:
        return 1
    else:
        return 0


def main():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    n = numroots(a, b, c)
    print("the number of roots is:", n)


main()
