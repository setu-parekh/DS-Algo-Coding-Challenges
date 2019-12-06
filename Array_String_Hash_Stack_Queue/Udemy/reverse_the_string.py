'''
QUESTION -
https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20SOLUTIONS/Sentence%20Reversal%20-%20SOLUTION.ipynb

APPROACH 1 -
    1. Splitting the string using 'split()' method to obtain the list of words.
    2. Reversing the order of elements in the list.
    3. Converting list to a string.

APPROACH 2 -
    1. Splitting the string using 'split()' method to obtain a list and then reversing the order of the list.
    2. Using 'join' function to concatenate the elements of the reversed list to an empty list.

APPROACH 3 -
    1. Instead of using the python function - 'split()', iterating through the string to find the start and end index of each word.
    2. Appending each word to a list and then reversing the list.

COMPLEXITY -
    1. Approach 1: O(N)
    2. Approach 2: O(N)
    3. Approach 3: O(N^2)

'''
# ______________________________________________________________________________________________________
'''
# Approach 1-

# Defining a method to create a reversed order list of the given string.
def reverseString1(string):
    word_list = string.strip().split()
    reverse_list = word_list[::-1]  # Way to reverse the elements of a list.
    return reverse_list

# Defining a method to convert a list to a string by defining an empty string and then concatenating the elements.
def listToString(list):
    string = " "
    for element in list:
        string = string + " " + element
    print(string)

reversed_words_list = reverseString1("Hi John,  are you ready to go?")
listToString(reversed_words_list)
'''
# ______________________________________________________________________________________________________
'''
# Approach 2-

# Defining a method using 'join' function to concatenate the string instead of manually converting a list into a string.
def reverseString2(string):
    return " ".join(string.split()[::-1])

print(reverseString2("  My name is Setu  "))
'''
# ______________________________________________________________________________________________________
# Approach 3 -

# Writing a method to split the string manually instead of using the in-built 'split()' function.
def reverseString3(string):
    # List to store each word of the string.
    words = []
    # Defining a list for space which will be used to identify the spaces in the string.
    space = [' ']
    i = 0
    # Iterating till the last alphabet of the string.
    while i < len(string):
        # Finding the start and end index of each word and appending it to the list - 'words'.
        if string[i] not in space:
            word_start = i
            while i < len(string) and string[i] not in space:
                i = i + 1
            words.append(string[word_start:i])
        else:
            i = i + 1

    return " ".join(reversed(words))

print(reverseString3("  Write a    method "))
