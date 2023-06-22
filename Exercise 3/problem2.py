# Ali Akbari 30171539

# charCounts function that returns a dictionary
def charCounts(s):
    # Dictionary of the alphabet
    alphabet = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
        'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13',
        'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19',
        't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
    }

    # Initialize variables
    dictionary = {}

    # Loop through alphabet dictionary
    for i in alphabet:
        # If the letter is in the string
        if i in s:
            # Add the letter and its value to the dictionary variable
            dictionary.update({i: alphabet[i]})
    # print and return the dictionary
    print(dictionary)
    return dictionary


# Main function
def main():
    # Get the two strings from the user
    str1 = input("What is the first string: ")
    str2 = input("What is the second string: ")

    # If they are equal to one another they are anagrams
    if charCounts(str1) == charCounts(str2):
        print("These strings are anagrams of each other!")

    # Otherwise they are not anagrams
    else:
        print("These strings are not anagrams of each other!")


main()
