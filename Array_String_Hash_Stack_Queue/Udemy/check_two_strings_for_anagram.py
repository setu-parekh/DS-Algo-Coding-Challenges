'''
QUESTION -
https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20PRACTICE/Anagram%20Check%20.ipynb

APPROACH -
    1. Replacing the spaces between the words with no space. Converting entire line into lower case.
    2. Creating a dictionary for storing each alphabet and its count into a dictionary format.
    3. Checking whether both strings are of same length and appending the alphabets and respective count of the 1st string into the dictionary.
    4. Looping through each alphabet of string 2 and subtracting the count of each alphabet stored in the dictionary. If both strings are Anagram, the ultimate count of each key of the dictionary will be '0'.

'''
def anagramChecker(line1, line2):
    # Replacing the spaces between the words with no space. Converting entire line into lower case.
    line1 = line1.replace(' ', '').lower()
    line2 = line2.replace(' ', '').lower()
    # Creating a dictionary for storing each alphabet and its count into a dictionary format.
    alphabet_counter = {}
    # Checking whether both strings are of same length and appending the alphabets and respective count into the dictionary.
    if len(line1) == len(line2):
        for alphabet in line1:
            if alphabet not in alphabet_counter.keys():
                alphabet_counter[alphabet] = 1
            else:
                alphabet_counter[alphabet] += 1
        # print("Pre", alphabet_counter)
        # For checking whether all the alphabets in the string 2 are exactly same as that of string 1, removing each alphabet one by one and checking whether the count of each is 0.
        for alphabet in line2:
            if alphabet in alphabet_counter.keys():
                alphabet_counter[alphabet] -= 1
            else:
                # print("This is not an Anagram")
                return False
        # print("Post", alphabet_counter)
        for value in alphabet_counter:
            if alphabet_counter[value] != 0:
                # print("This is not an Anagram")
                return False
        # print("Perfect Match!")
        return True

    else:
        print("Both strings are of different length")
        return False

print('1st Anagram: ', anagramChecker('cat', 'tac'))
print('2nd Anagram: ', anagramChecker('clint   eastwood', 'old west action'))
print('3rd Anagram: ', anagramChecker('My name is Setu Gandhi', 'My name is Neel Gandhi'))
