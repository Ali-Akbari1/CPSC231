# Ali Akbari 30171539

# main function to check if three lengths are able to make a triangle
def trianglecheck(length1, length2, length3):

    # check if any length is less than or equal to zero
    if (length1 <= 0 or length2 <= 0  or length3 <= 0):
        print("Please type a length greater than 0")
        return False

    # check if any one length is greater than or equal to the sum of the other two lengths
    elif (length1 + length2 <= length3) or (length1+length3 <= length2) or (length2+length3 <= length1):
        print("Those three values can not make a triangle")
        return False

    else:
        print("Those three values can make a triangle")
        return True


length1 = int(input("What is the first length of the triangle? "))
length2 = int(input("What is the second length of the triangle? "))
length3 = int(input("What is the third length of the triangle? "))

trianglecheck(length1, length2, length3)
