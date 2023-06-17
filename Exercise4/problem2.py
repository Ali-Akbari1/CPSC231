# Ali Akbari, 30171539

# Function sumRecursive that takes in myList as a parameter
def sumRecursive(myList):

    # Base case
    # Keep calling function until there is nothing in the list
    if len(myList) == 0:
        return 0
    # Add first element to the list
    # New list is everything after first element, and then repeat
    return myList[0] + sumRecursive(myList[1:])

# Main function
def main():

    # myList variable that will be passed to the function
    myList = [1, 2, 3, 4, 5]  # 15

    # Print the result of the sum of all the integers in a list
    # While also calling the function
    print(sumRecursive(myList))


main()
