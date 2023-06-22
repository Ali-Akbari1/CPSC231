def charCounts(s):
    dictionary = {}

    for i in s:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    print(dictionary)
    return dictionary


def main():
    str1 = input("What is the first string: ")
    str2 = input("What is the second string: ")

    count1 = charCounts(str1)
    count2 = charCounts(str2)

    if count1 == count2:
        print("These strings are anagrams of each other!")
    else:
        print("These strings are not anagrams of each other!")

    print(str1)
    print(str2)


main()
