'''
Question:
https://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20PRACTICE/Anagram%20Check%20.ipynb

'''
def anagramChecker(line1, line2):
# Replacing the spaces between the words with no space. Converting entire line into lower case.
    line1 = line1.replace(' ', '').lower()
    line2 = line2.replace(' ', '').lower()
# Creating a dictionary for storing each alphabet and its count int
    alphabet_counter = {}
