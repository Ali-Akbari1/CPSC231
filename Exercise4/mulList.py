
def sumRecursive(myList):

    if len(myList) == 0:
        return 0
    return myList[0] + sumRecursive(myList[1:])


def main():
    myList = [3, 4, 5]  # 12

    print(sumRecursive(myList))


main()
