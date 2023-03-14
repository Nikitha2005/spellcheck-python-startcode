# # Spell Check Starter
# # This start code creates two lists
# # 1: dictionary: a list containing all of the words from "dictionary.txt"
# # 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

# import re  # Needed for splitting text with a regular expression

# dictionary = ""
# aliceWords = ""

# def main():
#     # Load data files into lists
#     dictionary = loadWordsFromFile("data-files/dictionary.txt")
#     aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

#     # Print first 50 values of each list to verify contents
#     print(dictionary[0:50])
#     print(aliceWords[0:50])
# # end main()


# def loadWordsFromFile(fileName):
#     # Read file as a string
#     fileref = open(fileName, "r")
#     textData = fileref.read()
#     fileref.close()

#     # Split text by one or more whitespace characters
#     return re.split('\s+', textData)
# # end loadWordsFromFile()


# # Call main() to begin program
# main()

# def selOne(anArray, item):
#     for i in range(0, len(anArray)):
#         if anArray[i] == item:
#             return i
   
#     return -1


# def selOne(input, dictionary, aliceWords):
#     for i in range(0, len(dictionary)):
#         if dictionary[i] == input:
#             return i
#     print()
    
#     return -1
    

# #  Main Menu
# print("Main Menu")
# print("1: Spell Check a Word(Linear Search)")
# print("2: Spell Check a Word(Binary Search)")
# print("3: Spell Check Alice in Wonderland(Linear Search)")
# print("4: Spell Check Alice in Wonderland(Binary Search)")
# print("5: EXIT")

# selection = input("Enter Selection (1-5): ")

# # Selection Return Order
# if(selection == "1"):
#     input = input("Enter a Word to search:")
#     print(selOne(input, dictionary, aliceWords))

# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re
import bisect

dictionary = []
aliceWords = []


def main():
    global dictionary, aliceWords
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])


def loadWordsFromFile(fileName):
    # Read file as a string
    with open(fileName, "r") as file:
        textData = file.read()

    # Split text by one or more whitespace characters
    return re.findall(r'\w+', textData.lower())


def linear_search(input_word, word_list):
    for i in range(len(word_list)):
        if word_list[i] == input_word:
            return i
    return -1


def binary_search(input_word, word_list):
    index = bisect.bisect_left(word_list, input_word)
    if index != len(word_list) and word_list[index] == input_word:
        return index
    else:
        return -1


def check_spelling(text, dictionary, search_func):
    misspelled_words = set()
    for word in text:
        if search_func(word, dictionary) == -1:
            misspelled_words.add(word)
    print("Misspelled words:")
    print(misspelled_words)


if __name__ == '__main__':
    main()

    # Main Menu
    while True:
        print("Main Menu")
        print("1: Spell Check a Word (Linear Search)")
        print("2: Spell Check a Word (Binary Search)")
        print("3: Spell Check Alice in Wonderland (Linear Search)")
        print("4: Spell Check Alice in Wonderland (Binary Search)")
        print("5: EXIT")

        selection = input("Enter Selection (1-5): ")

        if selection == "1":
            input_word = input("Enter a word to search: ")
            result = linear_search(input_word, dictionary)
            if result != -1:
                print(f"'{input_word}' found at index {result} in the dictionary")
            else:
                print(f"'{input_word}' not found in the dictionary")

        elif selection == "2":
            input_word = input("Enter a word to search: ")
            result = binary_search(input_word, dictionary)
            if result != -1:
                print(f"'{input_word}' found at index {result} in the dictionary")
            else:
                print(f"'{input_word}' not found in the dictionary")

        elif selection == "3":
            check_spelling(aliceWords, dictionary, linear_search)

        elif selection == "4":
            check_spelling(aliceWords, dictionary, binary_search)

        elif selection == "5":
            break

        else:
            print("Invalid selection. Try again.")