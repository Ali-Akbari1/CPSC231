# Ali Akbari 30171539

# password function to check the strength of a password
def passwordcheck(password):
    hasDigit = False
    hasUpperCaseCharacter = False
    hasLowerCaseCharacter = False

    # if password is greater than eight characters
    if len(password) >= 8:

        # check for a number, lowercase and uppercase letter in the password
        # if password has number lowercase and uppercase letter return true
        # otherwise return false
        for char in password:
            if char.isdigit():
                hasDigit = True
            if char.isupper():
                hasUpperCaseCharacter = True
            if char.islower():
                hasLowerCaseCharacter = True
    else:
        return False

    return hasDigit and hasUpperCaseCharacter and hasLowerCaseCharacter


# main function to get input from user and print if it is a strong or weak password
def main():

    # get password from user
    password = str(input("Enter a password to check its strength "))

    # if password check function is true print it is a strong password
    # otherwise print it is a not a strong password
    if passwordcheck(password):
        print("That is a strong password")
    else:
        print("That is not a strong password")


main()

