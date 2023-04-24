# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def linearSearch(anArray, item):
    for i in range(0, len(anArray)):
        if anArray[i] == item:
            return i
   
    return -1

def binarySearch(anArray, item):
    low = 0
    
    high = len(anArray) - 1
    while low <= high:
        mid = (low + high) // 2
        if anArray[mid] == item:
            return mid
        elif anArray[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
    
    print("1: Spell Check a Word (Linear Search)")
    print("2: Spell Check a Word (Binary Search)")
    print("3: Spell Check Alice In Wonderland (Linear Search)")
    print("4: Spell Check Alice In Wonderland (Binary Search)")
    print("5: Exit")
    selection = int(input("Enter Selection:"))

    #  Selection 1: Spell Check a Word (Linear Search)
    if selection == 1:
        start = time.time()
        wordAsk = input("Enter a Word:").lower()
        process = linearSearch(dictionary,wordAsk)
        print("Liner Search Starting....")
        # Linear Search for word in dictionary and output results
        if process == -1:
            print(wordAsk, "was not found in dictionary")
        else:
            print(wordAsk, "was found at position", process)
        end = time.time()
        print(end - start)
            
    # Selection 2: Spell Check a Word (Binary Search) 
    elif selection == 2:
        start1 = time.time()
        wordAsk = input("Enter a Word:").lower()
        process = binarySearch(dictionary,wordAsk)
        print("Binary Search Starting....")
        # Binary Search for word in dictionary and output results
        if process == -1:
            print(wordAsk, "was not found in dictionary")
        else:
            print(wordAsk, "was found at position", process)
        end1 = time.time()
        print(end1 - start1)

    # Seleciton 3: Alice Words (Linear Search)
    elif selection == 3:
        start2 = time.time()
        count = 0
        for i in range(len(aliceWords)):
            # Linear serch for alice words in dictionary and cound words not found
            process = linearSearch(dictionary, aliceWords[i].lower())
            if process == -1:
                count += 1
           
        print(count, "words not found in dictionary")
        end2 = time.time()
        print(end2 - start2)
        
    
    # Selection 4: ALice Words (Binary Search)
    elif selection == 4:
        start3 = time.time()
        count = 0
        for i in range(len(aliceWords)):
            process = binarySearch(dictionary, aliceWords[i].lower())
            # Binary serch for alice words in dictionary and cound words not found
            if process == -1:
                count += 1
        print(count,"number of words not found in dictionary")
        end3 = time.time()
        print(end3 - start3)
        
    print("EXIT")
   

# Call main() to begin program
main()