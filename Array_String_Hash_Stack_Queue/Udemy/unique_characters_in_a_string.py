'''
QUESTION -
https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20PRACTICE/Unique%20Characters%20in%20String.ipynb

APPROACH -
    1. Create a count dictionary for each letter in the string.
    2. While iterating through each letter of the string, if it does not exist in the dictionary then make the count = 1.
    3. If that letter already exists in the dictionary, then return False and break the loop.
    4. Using 'get()' function will directly search for that letter and save iterating through the dictionary to search for a particular key.

TIME COMPLEXITY -
    1. Best Case - O(1) if we encounter repeated letters in the starting itself. The program will end and return False.
    2. Average Case - O(N)

'''
#
def checkUniqueCharacter(string):
    count_dict = {}
    for letter in string:
        if count_dict.get(letter) is None:
            count_dict[letter] = 1
        else:
            return False
    return True

print(checkUniqueCharacter('aabcde'))
